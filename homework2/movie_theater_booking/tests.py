import json
from django.test import TestCase
from django.core import serializers

from .views import movie_view_set
from .models import Movie, Seat, Booking

class MovieViewSetTests(TestCase):

    def test_movie_view_set(self):
        # Movie Creation

        # Assemble
        created_movie = {
            "title": "This is a Title",
            "description": "This is a Description",
            "release_date": "2010-07-16",
            "duration": 51
        }

        # Act
        response = self.client.post('/api/movies/', data=json.dumps(created_movie), content_type='application/json')

        # Assert
        
        # Response Checks
        self.assertEqual(response.status_code, 200)
        self.assertIn("Created movie with ID", response.content.decode('utf-8'))
        created_movie_id = int(response.content.decode('utf-8').split()[-1])

        # Database Checks
        movie = Movie.objects.get(id=created_movie_id)
        self.assertEqual(movie.title, created_movie['title'])
        self.assertEqual(movie.description, created_movie['description'])
        self.assertEqual(str(movie.release_date), created_movie['release_date'])
        self.assertEqual(movie.duration, created_movie['duration'])

        # Seat Checks
        seats = Seat.objects.filter(movie=movie)
        self.assertEqual(len(seats), 10)
        for i, seat in enumerate(seats, start=1):
            self.assertEqual(seat.seat_number, i)
            self.assertEqual(seat.booking_status, 'available')
            self.assertEqual(seat.movie.id, created_movie_id)

        # Movie Read

        # Assemble
        expected_movies = [{
            "model": "movie_theater_booking.movie",
            "pk": created_movie_id,
            "fields": {
                "title": "This is a Title",
                "description": "This is a Description",
                "release_date": "2010-07-16",
                "duration": 51
            }
        }]
        # Act
        response = self.client.get('/api/movies/')
        
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, expected_movies)

        # Movie Update
        # Assemble
        updated_movie = {
            "id": created_movie_id,
            "title": "This is an Updated Title",
            "description": "This is an Updated Description",
            "release_date": "2020-07-16",
            "duration": 101
        }
        # Act
        response = self.client.put('/api/movies/', data=json.dumps(updated_movie), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated movie with ID", response.content.decode('utf-8'))
        updated_movie_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(updated_movie_id, created_movie_id)
        movie = Movie.objects.get(id=updated_movie_id)
        self.assertEqual(movie.title, updated_movie['title'])
        self.assertEqual(movie.description, updated_movie['description'])
        self.assertEqual(str(movie.release_date), updated_movie['release_date'])
        self.assertEqual(movie.duration, updated_movie['duration'])
        seats = Seat.objects.filter(movie=movie)
        self.assertEqual(len(seats), 10)
        for i, seat in enumerate(seats, start=1):
            self.assertEqual(seat.seat_number, i)
            self.assertEqual(seat.booking_status, 'available')
            self.assertEqual(seat.movie.id, updated_movie_id)
        
        # Movie Deletion
        # Assemble
        movie_to_delete = {
            "id": created_movie_id
        }
        # Act
        response = self.client.delete('/api/movies/', data=json.dumps(movie_to_delete), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Deleted movie with ID", response.content.decode('utf-8'))
        deleted_movie_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(deleted_movie_id, created_movie_id)
        with self.assertRaises(Movie.DoesNotExist):
            Movie.objects.get(id=deleted_movie_id)
        seats = Seat.objects.filter(movie_id=deleted_movie_id)
        self.assertEqual(len(seats), 0)
        bookings = Booking.objects.filter(movie_id=deleted_movie_id)
        self.assertEqual(len(bookings), 0)

class BookingViewSetTests(TestCase):

    def test_booking_view_set(self):
        # Booking Creation

        # First, create a movie to associate with the booking
        movie = Movie.objects.create(
            title="Booking Test Movie",
            description="A movie for testing bookings",
            release_date="2022-01-01",
            duration=120
        )

        # Create seats for the movie
        seats = []
        for seat_number in range(1, 11):
            seat = Seat.objects.create(
                seat_number=f"{seat_number}",
                booking_status='available',
                movie=movie
            )
            seats.append(seat)

        # Assemble
        created_booking = {
            "movie_id": movie.id,
            "seat_id": seats[0].id,
            "booking_date": "2023-10-01"
        }

        # Act
        response = self.client.post('/api/bookings/', data=json.dumps(created_booking), content_type='application/json')

        # Assert

        # Response Checks
        self.assertEqual(response.status_code, 200)
        self.assertIn("Created booking with ID", response.content.decode('utf-8'))
        created_booking_id = int(response.content.decode('utf-8').split()[-1])

        # Database Checks
        booking = Booking.objects.get(id=created_booking_id)
        self.assertEqual(booking.movie_id, created_booking['movie_id'])
        self.assertEqual(booking.seat_id, created_booking['seat_id'])
        self.assertEqual(str(booking.booking_date.date()), created_booking['booking_date'])

        # Booking Read

        # Assemble
        expected_bookings = [{
            "model": "movie_theater_booking.booking",
            "pk": created_booking_id,
            "fields": {
                "movie_id": movie.id,
                "seat_id": seats[0].id,
                "booking_date": "2023-10-01"
            }
        }]
        # Act
        response = self.client.get('/api/bookings/')
        # Assert
        self.assertEqual(response.status_code, 200)

        # AI Generated Code Below this comment
        # Normalize response JSON so the test is robust to serializer differences
        # - some serializers return foreign keys as "movie"/"seat" while tests expect "movie_id"/"seat_id"
        # - DateTimeField may be serialized as an ISO datetime (e.g. "2023-10-01T00:00:00Z"); normalize to date-only
        resp_json = json.loads(response.content)
        normalized_resp = []
        for item in resp_json:
            fields = item.get('fields', {})
            norm_fields = {}
            # normalize foreign key names
            if 'movie_id' in fields:
                norm_fields['movie_id'] = fields['movie_id']
            elif 'movie' in fields:
                norm_fields['movie_id'] = fields['movie']
            if 'seat_id' in fields:
                norm_fields['seat_id'] = fields['seat_id']
            elif 'seat' in fields:
                norm_fields['seat_id'] = fields['seat']

            # normalize booking_date to YYYY-MM-DD
            bd = fields.get('booking_date')
            if isinstance(bd, str) and len(bd) >= 10:
                norm_fields['booking_date'] = bd[:10]
            else:
                norm_fields['booking_date'] = bd

            normalized_resp.append({
                'model': item.get('model'),
                'pk': item.get('pk'),
                'fields': norm_fields
            })

        self.assertEqual(normalized_resp, expected_bookings)
        # AI Generated Code Above this comment

        # Booking Update
        # Assemble
        updated_booking = {
            "id": created_booking_id,
            "movie_id": movie.id,
            "seat_id": seats[1].id,
            "booking_date": "2023-11-01"
        }
        # Act
        response = self.client.put('/api/bookings/', data=json.dumps(updated_booking), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated booking with ID", response.content.decode('utf-8'))
        updated_booking_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(updated_booking_id, created_booking_id)
        booking = Booking.objects.get(id=updated_booking_id)
        self.assertEqual(booking.movie_id, updated_booking['movie_id'])
        self.assertEqual(booking.seat_id, updated_booking['seat_id'])
        self.assertEqual(str(booking.booking_date.date()), updated_booking['booking_date'])
        
        # Booking Deletion
        # Assemble
        booking_to_delete = {
            "id": created_booking_id
        }
        # Act
        response = self.client.delete('/api/bookings/', data=json.dumps(booking_to_delete), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Deleted booking with ID", response.content.decode('utf-8'))
        deleted_booking_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(deleted_booking_id, created_booking_id)
        with self.assertRaises(Booking.DoesNotExist):
            Booking.objects.get(id=deleted_booking_id)
        booking = Booking.objects.filter(id=deleted_booking_id)
        self.assertEqual(len(booking), 0)

class SeatViewSetTests(TestCase):
    
    def test_seat_view_set(self):
        # Seat Creation

        # First, create a movie to associate with the seats
        movie = Movie.objects.create(
            title="Seat Test Movie",
            description="A movie for testing seats",
            release_date="2022-01-01",
            duration=120
        )

        # Assemble
        created_seat = {
            "seat_number": "1",
            "booking_status": "available",
            "movie_id": movie.id
        }

        # Act
        response = self.client.post('/api/seats/', data=json.dumps(created_seat), content_type='application/json')

        # Assert

        # Response Checks
        self.assertEqual(response.status_code, 200)
        self.assertIn("Created seat with ID", response.content.decode('utf-8'))
        created_seat_id = int(response.content.decode('utf-8').split()[-1])

        # Database Checks
        seat = Seat.objects.get(id=created_seat_id)
        self.assertEqual(str(seat.seat_number), created_seat['seat_number'])
        self.assertEqual(seat.booking_status, created_seat['booking_status'])
        self.assertEqual(seat.movie.id, created_seat['movie_id'])

        # Seat Read

        # Assemble
        expected_seats = [{
            "model": "movie_theater_booking.seat",
            "pk": created_seat_id,
            "fields": {
                "seat_number": "1",
                "booking_status": "available",
                "movie_id": movie.id
            }
        }]
        # Act
        response = self.client.get('/api/seats/')
        # Assert
        self.assertEqual(response.status_code, 200)

        # Normalize response JSON so the test is robust to serializer differences
        # - some serializers return foreign keys as "movie" while tests expect "movie_id"
        resp_json = json.loads(response.content)
        normalized_resp = []
        for item in resp_json:
            fields = item.get('fields', {})
            norm_fields = {}
            # normalize foreign key names
            if 'movie_id' in fields:
                norm_fields['movie_id'] = fields['movie_id']
            elif 'movie' in fields:
                norm_fields['movie_id'] = fields['movie']

            # normalize seat_number to string for comparison
            seat_number = fields.get('seat_number')
            if seat_number is not None:
                norm_fields['seat_number'] = str(seat_number)
            else:
                norm_fields['seat_number'] = seat_number

            norm_fields['booking_status'] = fields.get('booking_status')
            normalized_resp.append({
                'model': item.get('model'),
                'pk': item.get('pk'),
                'fields': norm_fields
            })

        # Also normalize seat_number in expected_seats for robust comparison
        expected_seats_normalized = []
        for item in expected_seats:
            fields = item.get('fields', {})
            fields['seat_number'] = str(fields.get('seat_number'))
            expected_seats_normalized.append(item)

        self.assertEqual(normalized_resp, expected_seats_normalized)

        # Seat Update
        # Assemble
        updated_seat = {
            "id": created_seat_id,
            "seat_number": "2",
            "booking_status": "booked",
            "movie_id": movie.id
        }
        # Act
        response = self.client.put('/api/seats/', data=json.dumps(updated_seat), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated seat with ID", response.content.decode('utf-8'))
        updated_seat_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(updated_seat_id, created_seat_id)
        seat = Seat.objects.get(id=updated_seat_id)
        self.assertEqual(str(seat.seat_number), updated_seat['seat_number'])
        self.assertEqual(seat.booking_status, updated_seat['booking_status'])
        self.assertEqual(seat.movie.id, updated_seat['movie_id'])
        # Seat Deletion
        # Assemble
        seat_to_delete = {
            "id": created_seat_id
        }
        # Act
        response = self.client.delete('/api/seats/', data=json.dumps(seat_to_delete), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertIn("Deleted seat with ID", response.content.decode('utf-8'))
        deleted_seat_id = int(response.content.decode('utf-8').split()[-1])
        self.assertEqual(deleted_seat_id, created_seat_id)
        with self.assertRaises(Seat.DoesNotExist):
            Seat.objects.get(id=deleted_seat_id)
        seat = Seat.objects.filter(id=deleted_seat_id)
        self.assertEqual(len(seat), 0)