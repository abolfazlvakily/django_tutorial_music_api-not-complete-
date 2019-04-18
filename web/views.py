from django.shortcuts import render, redirect
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def register(request):
    logout(request)
    if request.method == 'POST':
        if 'username' and 'email' and 'password' in request.POST:
            this_user = request.POST['username']
            this_email = request.POST['email']
            this_password = request.POST['password']
            user = authenticate(username=this_user, password=this_password)
            if user is not None:
                return JsonResponse({'status': 'this account is exist'}, encoder=JSONEncoder, safe=False)
            else:
                User.objects.create_user(this_user, this_email, this_password)
                login(request, user)
                message = {}
                message['status'] = 'ok'
                message['message'] = 'You are logged in'
                return JsonResponse(message, encoder=JSONEncoder, safe=False)
    else:
        return render(request, 'register.html')


@csrf_exempt
def login_form(request):
    if 'username' and 'password' in request.POST:
        this_user = request.POST['username']
        this_password = request.POST['password']
        user = authenticate(username=this_user, password=this_password)
        if user is not None:
            login(request, user)
            return redirect('/api/')
        else:
            return JsonResponse({'status': 'account not found. please signup'}, encoder=JSONEncoder, safe=False)
    else:
        return render(request, 'login.html')


@csrf_exempt
def logout_form(request):
    logout(request)
    return JsonResponse({'status': 'ok'}, encoder=JSONEncoder, safe=False)
