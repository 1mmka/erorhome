from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse

def list_users(request):
    response = requests.get('http://127.0.0.1:8000/')
    tasks = response.json()
    return render(request, 'list.html', {'tasks':tasks})

def login_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            data = {
                'username' : username,
                'password' : password,
            }
            send_request = requests.post('http://127.0.0.1:8000/login/',data)
        
            if send_request.status_code == 200:
                return HttpResponse('Successfully sent data')
            else:
                return HttpResponse('Forbidden')
        else:
            return HttpResponse('Invalid data provided')
    else:
        return render(request,'login.html')