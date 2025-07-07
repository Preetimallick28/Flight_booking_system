from django.urls import path
from base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('details_page/<int:pk>/', views.flight_details_page, name='details_page'),
    path('book_now/<int:pk>/', views.book_now, name='book_now'),
    path('passanger_details/', views.passenger, name='passenger_details'),
    path('passenger_edit/<int:pk>', views.edit_passenger, name='edit_passenger'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_passanger/<int:pk>', views.delete_passanger, name='delete_passenger'),
    path('history',views.history,name='history'),
    path('restore_task/<int:pk>',views.restore_task,name='restore_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
]
