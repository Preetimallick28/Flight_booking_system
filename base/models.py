from django.db import models

# Create your models here.
class flight_company_model(models.Model):
    flight_company = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_company 

class flight_details(models.Model):
    flight_company = models.ForeignKey(flight_company_model,on_delete=models.CASCADE)
    flight_name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    destination_time = models.CharField(max_length=100)
    seat_availibility = models.CharField(max_length=100)

    def __str__(self):
         return f"{self.flight_name} | {self.departure} -> {self.destination} | ₹{self.price}"

class passenger_details(models.Model):
    flight = models.ForeignKey(flight_details, on_delete=models.CASCADE, null=True)
    
    # Flight fields duplicated here
    flight_name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    destination_time = models.CharField(max_length=100)
    
    # Passenger info
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} | {self.flight_name} ({self.departure} → {self.destination})"

class history_model(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=100)
    flight_name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    destination_time = models.CharField(max_length=100)
    

