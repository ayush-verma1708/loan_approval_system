from django.urls import path
from base import views

urlpatterns = [
    path('test/',views.test,name="Test"),
    path('register/',views.register_customer,name="Register Customer"),
    path('form/',views.register_form,name="Register "),
    path('user/<int:pk>/', views.user_response_page, name='user_response'),
    path('user/', views.user_page, name='user'),
    path('delete/', views.delete_all, name='delete'),
    path('check_eligiblity/', views.check_eligibility, name='delete'),
]