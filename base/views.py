from django.shortcuts import render , redirect , get_object_or_404
from base.models import flight_company_model,flight_details,passenger_details,history_model
# Create your views here.

def home(request):
    flight = flight_company_model.objects.all() 
    return render(request,'home.html',{'flightnames':flight})

# def flight_details_page(request,pk):    
#     specific_flight = flight_details.objects.get(id=pk)
#     return render(request,'details.html',{'data':specific_flight})

def flight_details_page(request, pk):    
    specific_flight_details = flight_details.objects.filter(flight_company=pk)
    return render(request, 'details.html', {'flight_data': specific_flight_details,'name':pk})

def book_now(request, pk):
    book = get_object_or_404(flight_details, pk=pk)

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        aadhar_number = request.POST['aadhar_number']

        passenger_details.objects.create(
            flight=book,
            flight_name=book.flight_name,
            departure=book.departure,
            destination=book.destination,
            price=book.price,
            departure_time=book.departure_time,
            destination_time=book.destination_time,
            name=name,
            age=age,
            phone=phone,
            email=email,
            aadhar_number=aadhar_number
        )

        return redirect('passenger_details')  # or a confirmation page

    return render(request, 'book_now.html', {'book': book})


def passenger(request):    
    passenger_data = passenger_details.objects.all()
    return render(request,'passenger_details.html',{'passengerdata':passenger_data})


def edit_passenger(request,pk):
    data = passenger_details.objects.get(id=pk)
    if request.method == 'POST':
        name_Data = request.POST['name']
        age_Data = request.POST['age']
        phone_Data = request.POST['phone']
        email_Data = request.POST['email']
        aadhar_Data = request.POST['aadhar_number']

        # override
        # student.sname - old data
        # name_Data - new data
        data.name = name_Data  
        data.age = age_Data
        data.phone = phone_Data
        data.email = email_Data
        data.aadhar_number = aadhar_Data
        data.save()
        return redirect('passenger_details')

    return render(request,'passanger_edit.html',{'data':data})

def confirm_delete(request,pk):
    task=passenger_details.objects.get(id=pk)
    return render(request,'confirm_delete.html',{'task':task})


def delete_passanger(request,pk):
    del_pass = passenger_details.objects.get(id=pk)
    history_model.objects.create(
        name = del_pass.name,
        age = del_pass.age,
        phone = del_pass.phone,
        email = del_pass.email,
        aadhar_number = del_pass.aadhar_number,
        flight_name = del_pass.flight_name,
        departure = del_pass.departure,
        price = del_pass.price,
        destination = del_pass.destination,
        departure_time = del_pass.departure_time,
        destination_time = del_pass.destination_time,
    )
    del_pass.delete()
    return redirect('history')

def history(request):
    history_Data = history_model.objects.all()
    return render(request,'history.html',{'historydata':history_Data})

def restore_task(request,pk):
    restore_data = history_model.objects.get(id=pk)
    print(restore_data)
    passenger_details.objects.create(
        name = restore_data.name,
        age = restore_data.age,
        phone = restore_data.phone,
        email = restore_data.email,
        aadhar_number = restore_data.aadhar_number,
        departure = restore_data.departure,
        destination = restore_data.destination,
        flight_name = restore_data.flight_name,
        destination_time = restore_data.destination_time,
        departure_time = restore_data.departure_time,
        price = restore_data.price

    )
    restore_data.delete()
    return render(request,'passenger_details.html')
    
def delete_task(request,pk):
    delete_task = history_model.objects.get(id=pk)
    delete_task.delete()

    return redirect('passenger_details')
