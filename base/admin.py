from django.contrib import admin
from base.models import flight_companies , flight_details , bookModel , historyModel
# Register your models here.
class flightCompaniesAdmin(admin.ModelAdmin):
    list_display=['flight_company_name']

class flightDetailsAdmin(admin.ModelAdmin):
    list_display=['flight_company_name',
                  'flight_name',
                  'flight_departure',
                  'flight_destination',
                  'flight_departure_time',
                  'flight_destination_time',
                  'flight_ticket_price'
                  ]
class bookAdminModel(admin.ModelAdmin):
    list_display=[
        'flight_name',
        'flight_departure',
        'flight_destination',
        'flight_departure_time',
        'flight_destination_time',
        'flight_ticket_price',
        'passenger_name',
        'passenger_age',
        'passenger_gender',
        'passenger_phone',
        'passenger_email',
        'passenger_aadhar',
    ]
class bookAdminModel(admin.ModelAdmin):
    list_display=[
        'flight_name',
        'flight_departure',
        'flight_destination',
        'flight_departure_time',
        'flight_destination_time',
        'flight_ticket_price',
        'passenger_name',
        'passenger_age',
        'passenger_gender',
        'passenger_phone',
        'passenger_email',
        'passenger_aadhar',
    ]
class historyAdminModel(admin.ModelAdmin):
    list_display=[
        'flight_name',
        'flight_departure',
        'flight_destination',
        'flight_departure_time',
        'flight_destination_time',
        'flight_ticket_price',
        'passenger_name',
        'passenger_age',
        'passenger_gender',
        'passenger_phone',
        'passenger_email',
        'passenger_aadhar',
    ]

admin.site.register(flight_companies,flightCompaniesAdmin)
admin.site.register(flight_details,flightDetailsAdmin)
admin.site.register(bookModel,bookAdminModel)
admin.site.register(historyModel,historyAdminModel)