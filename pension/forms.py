from .models import Room, Reservation, Comment
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))


class ReservationForm(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    surname = forms.CharField(max_length=20,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}))
    date_from = forms.DateField(required=True,
                                widget=forms.DateInput(attrs={'placeholder': 'e.g.: 15-03-2019', 'type': "date"}),
                                )
    date_to = forms.DateField(required=True,
                              widget=forms.DateInput(attrs={'placeholder': 'e.g.: 15-03-2019', 'type': "date"}),
                              )
    room = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label="Select room:")
