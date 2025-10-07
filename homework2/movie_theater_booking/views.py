import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie, Booking, Seat
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def movie_view_set(request):
    if request.method == 'POST':
        # Create
        data = json.loads(request.body)
        new_movie = Movie()
        new_movie.title = data['title']
        new_movie.description = data['description']
        new_movie.release_date = data['release_date']
        new_movie.duration = data['duration']
        new_movie.save()

        # Create 10 seats for the new movie
        for seat_number in range(1, 11):
            seat = Seat()
            seat.seat_number = f"{seat_number}"
            seat.booking_status = 'available'
            seat.movie = new_movie
            seat.save()

        return HttpResponse(f"Created movie with ID {new_movie.id}")

    if request.method == 'GET':
        # Read
        movies = Movie.objects.all()
        movies_json = serializers.serialize('json', movies)
        return HttpResponse(movies_json, content_type='application/json')

    if request.method == 'PUT':
        # Update
        data = json.loads(request.body)
        movie_id = data['id']
        movie = Movie.objects.get(id=movie_id)
        movie.title = data['title']
        movie.description = data['description']
        movie.release_date = data['release_date']
        movie.duration = data['duration']
        movie.save()
        return HttpResponse(f"Updated movie with ID {movie_id}")

    if request.method == 'DELETE':
        # Delete
        data = json.loads(request.body)
        movie_id = data['id']
        movie = Movie.objects.get(id=movie_id)
        movie.delete()
        return HttpResponse(f"Deleted movie with ID {movie_id}")

def booking_view_set(request):
    if request.method == 'POST':
        # Create
        data = json.loads(request.body) 
        new_booking = Booking()
        new_booking.movie_id = data['movie_id']
        new_booking.seat_id = data['seat_id']
        new_booking.booking_date = data['booking_date']
        new_booking.save()
        return HttpResponse(f"Created booking with ID {new_booking.id}")
    
    if request.method == 'GET':
        # Read
        bookings = Booking.objects.all()
        bookings_json = serializers.serialize('json', bookings)
        return HttpResponse(bookings_json, content_type='application/json')
    if request.method == 'PUT':
        # Update
        data = json.loads(request.body)
        booking_id = data['id']
        booking = Booking.objects.get(id=booking_id)
        booking.movie_id = data['movie_id']
        booking.seat_id = data['seat_id']
        booking.booking_date = data['booking_date']
        booking.save()
        return HttpResponse(f"Updated booking with ID {booking_id}")

    if request.method == 'DELETE':
        # Delete
        data = json.loads(request.body)
        booking_id = data['id']
        booking = Booking.objects.get(id=booking_id)
        booking.delete()
        return HttpResponse(f"Deleted booking with ID {booking_id}")

def seat_view_set(request):
    if request.method == 'POST':
        # Create
        data = json.loads(request.body)
        new_seat = Seat()
        new_seat.movie_id = data['movie_id']
        new_seat.seat_number = data['seat_number']
        new_seat.booking_status = data['booking_status']
        new_seat.save()
        return HttpResponse(f"Created seat with ID {new_seat.id}")
    
    if request.method == 'GET':
        # Read
        seats = Seat.objects.all()
        seats_json = serializers.serialize('json', seats)
        return HttpResponse(seats_json, content_type='application/json')
    
    if request.method == 'PUT':
        # Update
        data = json.loads(request.body)
        seat_id = data['id']
        seat = Seat.objects.get(id=seat_id)
        seat.movie_id = data['movie_id']
        seat.seat_number = data['seat_number']
        seat.booking_status = data['booking_status']
        seat.save()
        return HttpResponse(f"Updated seat with ID {seat_id}")

    if request.method == 'DELETE':
        # Delete
        data = json.loads(request.body)
        seat_id = data['id']
        seat = Seat.objects.get(id=seat_id)
        seat.delete()
        return HttpResponse(f"Deleted seat with ID {seat_id}")
    
# Index
def index(request):
    return render(request, 'index.html')
# User views
def movie_view(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def seat_booking_view(request, movie_id):
    seats = Seat.objects.filter(movie_id=movie_id)
    return render(request, 'seat_booking.html', {'seats': seats})

def booking_history_view(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_history.html', {'bookings': bookings})

def book_seat(request, seat_id):
    seat = Seat.objects.get(id=seat_id)
    if seat.booking_status == 'available':
        seat.booking_status = 'booked'
        seat.save()
        # Create booking history entry
        new_booking = Booking()
        new_booking.movie = seat.movie
        new_booking.seat = seat
        new_booking.booking_date = datetime.datetime.now()
        new_booking.save()
        return render(request, 'book_seat.html', {'seat': seat})
    else:
        return HttpResponse(f"Seat {seat.seat_number} is already booked")
