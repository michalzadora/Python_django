from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pension'

urlpatterns = [
    # example : /pension/
    path('', views.index, name='index'),
    # example : /pension/4/
    path('<int:room_id>/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('comment/', views.comment, name='comment'),
    path('reservation/', views.reservation, name='reservation'),
]
