from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('flight_details_list/<str:pk>',views.flight_details_list,name='flight_details_list'),
    path('book_passenger/<str:pk>',views.book_passenger,name='book_passenger'),
    path('booking_list',views.booking_list,name='booking_list'),
    path('update/<int:pk>',views.update_passenger_list,name='update'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_passenger_data/<int:pk>',views.delete_passenger_data,name='delete_passenger_data'),
    path('history_passenger_data',views.history_passenger_data,name='history_passenger_data'),
    path('history_delete/<int:pk>',views.history_delete,name='history_delete'),
    path('restore_data/<int:pk>',views.restore_data,name='restore_data'),

]
