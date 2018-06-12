from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils import timezone
from .forms import CommentForm, ReservationForm
from .models import Comment, Room, Reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def welcome(request):
    return render(request, 'pension/welcome.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('pension:index')
    else:
        form = UserCreationForm()
    return render(request, 'authorisation/register.html', {'form': form})


@login_required
def index(request):
    rooms = Room.objects.order_by('name')
    comments = Comment.objects.order_by('-date_added')[:2]
    context = {'rooms': rooms, 'comments': comments}
    return render(request, 'pension/index.html', context)


@login_required
def detail(request, room_id):
    rooms = Room.objects.order_by('name')
    context = {'rooms': rooms}
    room = get_object_or_404(Room, pk=room_id)
    template_name = 'pension/detail.html'
    context = {'room': room, 'rooms': rooms}
    return render(request, template_name, context)


@login_required
def contact(request):
    rooms = Room.objects.order_by('name')
    context = {'rooms': rooms}
    template_name = 'pension/contact.html'
    context = {'rooms': rooms}
    return render(request, template_name, context)


@login_required
def reservation(request):
    rooms = Room.objects.order_by('name')
    reservations = Reservation.objects.order_by('reservation_date')
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = Reservation(user=request.user,
                                          date_from=request.POST['date_from'],
                                          date_to=request.POST['date_to'],
                                          room=get_object_or_404(Room, pk=request.POST['room']),
                                          name=request.POST['name'], surname=request.POST['surname'])
            new_reservation.save()
            return redirect('pension:index')
        else:
            print(form.errors)
    else:
        form = ReservationForm()
    context = {'rooms': rooms, 'form': form}
    return render(request, 'pension/reservation.html', context)


@login_required
def comment(request):
    rooms = Room.objects.order_by('name')
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('pension:index')
    else:
        form = CommentForm()
    context = {'rooms': rooms, 'form': form}
    return render(request, 'pension/comment.html', context)
