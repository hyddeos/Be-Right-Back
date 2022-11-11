from datetime import timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.parsers import JSONParser
from brb.serializers import AwaySerializer
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import timedelta
from .models import Away, User


# Create your views here.
def index(request):

    data = Away.objects.all()[0]
    print("Current Data", data)
    user = request.user
    current_time = timezone.now()
    print("time NOW:", current_time)
    status = data.active

    if request.method == "POST":
        if 'reset' in request.POST:
            data.active = False
            data.save()
            print("Data now False")
            return render(request, 'brb/index.html', {
                "user": user,
                "time": current_time,
                "status": data.active,
            })
        else:
            reason = request.POST["reason"]
            hours = int(request.POST["hour"])
            minutes = int(request.POST["minute"])
            print("In post", hours, type(hours), minutes, type(minutes))

            if hours > 0 and hours < 24 and minutes >= 0 and minutes < 60:
                data.reason = reason
                data.return_time = current_time + timedelta(hours=hours, minutes=minutes)
                data.active = True
                data.save()
            
                return render(request, 'brb/index.html', {
                "user": user,
                "time": current_time,
                "status": data.active,
                "data": data,
            })
            else:
                print("Input Check Failed")
                return render(request, "brb/index.html", {
                "message": "Input Error, Try Again!",
                "user": user,
                "time": str(current_time),
                "status": status,
                })

    else:    

        return render(request, 'brb/index.html', {
            "user": user,
            "time": current_time,
            "status": data.active,
            "data": data,
        })


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("startpage"))
        else:
            return render(request, "brb/login.html", {
                "message": "Error Invalid username and/or password."
            })
    else:
        return render(request, "brb/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("startpage"))

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "brb/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "brb/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("startpage"))
    else:
        return render(request, "brb/register.html")


def api(request):
    if request.method == 'GET':
        away = Away.objects.all()
        serializer = AwaySerializer(Away, many=True)
        return JsonResponse(serializer.data, safe=False)