from django.db import models
from django.contrib.auth.models import User
class ParkingOwner(models.Model):
    parking_owner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    cars = models.ManyToManyField('Car', related_name='drivers')
    bookings = models.ManyToManyField('Booking', related_name='drivers')
    reviews = models.ManyToManyField('Review', related_name='drivers')

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

# class Booking(models.Model):
#     booking_id = models.AutoField(primary_key=True)
#     driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='bookings')
#     car = models.ForeignKey('Car', on_delete=models.CASCADE)
#     parking_lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    assigned_driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='assigned_bookings')
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    parking_lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

# class ParkingLot(models.Model):
#     parking_lot_id = models.AutoField(primary_key=True)
#     address = models.TextField()
#     capacity = models.IntegerField()
#     space_availability = models.IntegerField()
#     parking_owner = models.ForeignKey('ParkingOwner', on_delete=models.CASCADE)
class ParkingLot(models.Model):
    parking_lot_id = models.AutoField(primary_key=True)
    address = models.TextField()
    capacity = models.IntegerField()
    space_availability = models.IntegerField()
    parking_owner = models.ForeignKey('ParkingOwner', on_delete=models.CASCADE)

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    license_plate_number = models.CharField(max_length=20)
    model = models.CharField(max_length=255)
    registration_year = models.IntegerField()

# class Review(models.Model):
#     review_id = models.AutoField(primary_key=True)
#     driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='reviews')
#     parking_lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     review_text = models.TextField()
#     date_submitted = models.DateField()
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='authored_reviews')
    parking_lot = models.ForeignKey('ParkingLot', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    date_submitted = models.DateField()
