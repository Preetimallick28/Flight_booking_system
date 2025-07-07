from django.contrib import admin
from base.models import flight_company_model, flight_details , passenger_details , history_model

# Register your models here.
class flightAdmincompany(admin.ModelAdmin):
    list_display=['flight_company']
class flightAdmindetails(admin.ModelAdmin):
    list_display=['flight_company','flight_name','departure','destination','price','departure_time','destination_time','seat_availibility']
class passengerAdmindetails(admin.ModelAdmin):
    list_display=['flight_name','departure','destination','price','departure_time','destination_time','name','age','phone','email','aadhar_number']
class historyAdmindetails(admin.ModelAdmin):
    list_display=['flight_name','departure','destination','price','departure_time','destination_time','name','age','phone','email','aadhar_number']

admin.site.register(flight_company_model,flightAdmincompany)
admin.site.register(flight_details,flightAdmindetails)
admin.site.register(passenger_details,passengerAdmindetails)
admin.site.register(history_model,historyAdmindetails)
