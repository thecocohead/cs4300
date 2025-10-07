"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movie_theater_booking.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/movies/', movie_view_set, name='movie_api'),
    path('api/bookings/', booking_view_set, name='booking_api'),
    path('api/seats/', seat_view_set, name='seat_api'),
    path('movies/', movie_view, name='movie_view'),
    path('seat_bookings/<int:movie_id>/', seat_booking_view, name='seat_booking_view'),
    path('booking_history/', booking_history_view, name='booking_history_view'),
    path('book_seat/<int:seat_id>/', book_seat, name='book_seat'),
]
