from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Customer, Task
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ListCustomersSerializer, CreateCustomerSerializer, UpdateCustomerSerializer, TaskListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

@api_view(['GET'])
def list_customers(request):
    queryset = Customer.objects.all()
    serializer = ListCustomersSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_tasks(request):
    queryset = Task.objects.all()
    serializer = TaskListSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)







@api_view(['GET'])
def retrieve_customer(request, pk):
    queryset = Customer.objects.filter(id=pk)
    serializer = ListCustomersSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_customer(request):
    serializer = CreateCustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_customer(request, pk):
    queryset = Customer.objects.filter(id=pk)
    serializer = UpdateCustomerSerializer(queryset, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_customer(request, pk):
    queryset = Customer.objects.filter(id=pk)
    queryset.delete()
    return Response(status=status.HTTP_200_OK)
    


def CustomLoginView(request):
    print(request.data)