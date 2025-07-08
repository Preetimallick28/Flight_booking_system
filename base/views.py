from django.shortcuts import render , redirect
from base.models import flight_companies , flight_details , bookModel , historyModel

# Create your views here.

def home(request):
    data = flight_companies.objects.all()
    return render(request,'flight_companies.html',{'data':data})

def about(request):
    return render(request,'about.html')

def flight_details_list(request,pk):
    data = flight_details.objects.filter(flight_company_name=pk)
    return render(request,'flight_details_list.html',{'data':data})

def book_passenger(request,pk):
    data = flight_details.objects.get(flight_name=pk)
    if request.method == 'POST':
        flight_name=request.POST['flight_name'],
        flight_departure = request.POST['flight_departure']
        flight_destination = request.POST['flight_destination']
        flight_departure_time = request.POST['flight_departure_time']
        flight_destination_time = request.POST['flight_destination_time']
        flight_ticket_price = request.POST['flight_ticket_price']
        passenger_name = request.POST['p_name']
        passenger_age = request.POST['p_age']
        passenger_gender = request.POST['p_gender']
        passenger_phone = request.POST['p_number']
        passenger_email = request.POST['p_email']
        passenger_aadhar = request.POST['p_aadhar']

        bookModel.objects.create(
            flight_name=flight_name,
            flight_departure=flight_departure,
            flight_destination=flight_destination,
            flight_departure_time=flight_departure_time,
            flight_destination_time=flight_destination_time,
            flight_ticket_price=flight_ticket_price,
            passenger_name=passenger_name,
            passenger_age=passenger_age,
            passenger_gender=passenger_gender,
            passenger_phone=passenger_phone,
            passenger_email=passenger_email,
            passenger_aadhar=passenger_aadhar
        )
        return redirect('booking_list')
    return render(request,'book_passenger.html',{'data':data})

def booking_list(request):
    data = bookModel.objects.all()
    return render(request,'booking_list.html',{'data':data})

def update_passenger_list(request,pk):
    data = bookModel.objects.get(id=pk)
    if request.method == 'POST':
        passenger_name = request.POST['p_name']
        passenger_age = request.POST['p_age']
        passenger_gender = request.POST['p_gender']
        passenger_phone = request.POST['p_number']
        passenger_email = request.POST['p_email']
        passenger_aadhar = request.POST['p_aadhar']

        data.passenger_name=passenger_name
        data.passenger_age = passenger_age
        data.passenger_gender = passenger_gender
        data.passenger_phone = passenger_phone
        data.passenger_email = passenger_email
        data.passenger_aadhar = passenger_aadhar

        data.save()
        return redirect('booking_list')


    return render(request,'update.html',{'data':data})

def confirm_delete(request,pk):
    data = bookModel.objects.get(id=pk)
    return render(request,'confirm_delete.html',{'data':data})
    


def delete_passenger_data(request,pk):
    data = bookModel.objects.get(id=pk)
    historyModel.objects.create(
        flight_name=data.flight_name,
        flight_departure=data.flight_departure,
        flight_destination=data.flight_destination,
        flight_departure_time=data.flight_departure_time,
        flight_destination_time=data.flight_destination_time,
        flight_ticket_price=data.flight_ticket_price,
        passenger_name=data.passenger_name,
        passenger_age=data.passenger_age,
        passenger_gender=data.passenger_gender,
        passenger_phone=data.passenger_phone,
        passenger_email=data.passenger_email,
        passenger_aadhar=data.passenger_aadhar
    )
    data.delete()   
    return redirect('history_passenger_data')

def history_passenger_data(request):
    data = historyModel.objects.all()
    return render(request,'history_passenger.html',{'data':data})

def history_delete(request,pk):
    data= historyModel.objects.get(id=pk)
    data.delete()
    return redirect('history_passenger_data')

def restore_data(request,pk):
    data = historyModel.objects.get(id=pk)
    bookModel.objects.create(
        flight_name=data.flight_name,
        flight_departure=data.flight_departure,
        flight_destination=data.flight_destination,
        flight_departure_time=data.flight_departure_time,
        flight_destination_time=data.flight_destination_time,
        flight_ticket_price=data.flight_ticket_price,
        passenger_name=data.passenger_name,
        passenger_age=data.passenger_age,
        passenger_gender=data.passenger_gender,
        passenger_phone=data.passenger_phone,
        passenger_email=data.passenger_email,
        passenger_aadhar=data.passenger_aadhar
    )
    data.delete()
    return redirect('booking_list')

