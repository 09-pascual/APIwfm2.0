# wfmapi/views/register.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from wfmapi.models import User  # Updated to your new app name

@csrf_exempt
def register_user(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
        
        # Create user using your custom model
        user = User.objects.create_user(
            email=data['email'],
            password=data['password'],
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            phone_number=data['phone_number'],
            is_owner=data.get('is_owner', False)
        )

        # Create authentication token
        token = Token.objects.create(user=user)
        
        return JsonResponse({
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "phone_number": user.phone_number,
            "is_owner": user.is_owner,
            "token": token.key
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
        user = authenticate(
            username=data['email'],  # Using email as username
            password=data['password']
        )

        if user:
            token = Token.objects.get(user=user)
            return JsonResponse({
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "is_owner": user.is_owner,
                "token": token.key
            })
        
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)