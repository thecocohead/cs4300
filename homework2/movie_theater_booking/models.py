from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField() 

class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # Outside of assignment spec to account for different movies
    seat_number = models.IntegerField()
    booking_status = models.TextField()

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()
