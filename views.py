# myapp/views.py
import json 
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def login(request):
    if request.method == 'POST':
        if 'application/json' in request.content_type:
            # Request from Postman or other API client
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            device = data.get('device', 'web')
        else:
            # Request from a web form
            username = request.POST.get('username')
            password = request.POST.get('password')
            device = 'web'

        print(username, password, device)

        if device == 'mobile':
            return JsonResponse({'message': 'Login successful From Mobile ', 'username': username})
        elif username == 'yogesh' and password:
            return render(request, 'success.html')
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=400)
    else:
        return render(request, 'login.html')

@csrf_exempt
def get_csrf_token(request):
    csrf_token = get_token(request)
    response = JsonResponse({'csrf_token': csrf_token})
    response.set_cookie('csrftoken', csrf_token)
    return response