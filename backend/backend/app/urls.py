from django.urls import path
from .views import ListCustomersView, RetrieveCustomerView, CreateCustomerView, UpdateCustomerView, DeleteCustomerView, list_customers, retrieve_customer, create_customer, update_customer, delete_customer,CustomLoginView


urlpatterns = [
    path('', list_customers, name='list'),
    path('<int:pk>/', retrieve_customer, name='retrieve'),
    path('create/', create_customer, name='create'),
    path('update/<int:pk>/', update_customer, name='update'),
    path('delete/<int:pk>/', delete_customer, name='delete'),
    
    
    path('login/',CustomLoginView,name='login-view')
]
