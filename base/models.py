from django.db import models

# Create your models here.

class flight_companies(models.Model):
    flight_company_name = models.CharField(max_length=100)

class flight_details(models.Model):
    flight_company_name = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    flight_departure = models.CharField(max_length=100)
    flight_destination = models.CharField(max_length=100)
    flight_departure_time = models.CharField(max_length=100)
    flight_destination_time = models.CharField(max_length=100)
    flight_ticket_price = models.CharField(max_length=100)

class bookModel(models.Model):
    flight_name = models.CharField(max_length=100)
    flight_departure = models.CharField(max_length=100)
    flight_destination = models.CharField(max_length=100)
    flight_departure_time = models.CharField(max_length=100)
    flight_destination_time = models.CharField(max_length=100)
    flight_ticket_price = models.CharField(max_length=100)
    passenger_name = models.CharField(max_length=100)
    passenger_age = models.CharField(max_length=100)
    passenger_gender = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=100)
    passenger_email = models.CharField(max_length=100)
    passenger_aadhar = models.CharField(max_length=100)

class historyModel(models.Model):
    flight_name = models.CharField(max_length=100)
    flight_departure = models.CharField(max_length=100)
    flight_destination = models.CharField(max_length=100)
    flight_departure_time = models.CharField(max_length=100)
    flight_destination_time = models.CharField(max_length=100)
    flight_ticket_price = models.CharField(max_length=100)
    passenger_name = models.CharField(max_length=100)
    passenger_age = models.CharField(max_length=100)
    passenger_gender = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=100)
    passenger_email = models.CharField(max_length=100)
    passenger_aadhar = models.CharField(max_length=100)
    