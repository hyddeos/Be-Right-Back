import os
from datetime import timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from brb.serializers import AwaySerializer
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import timedelta
from .models import Away
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .utils import auto_off
from dotenv import load_dotenv


# Create your views here.
def index(request):

    data = Away.objects.first()
    print("data", data)
    user = request.user
    current_time = timezone.localtime(timezone.now())
    # Check if there user has forgotten to remove Away-status
    if data.active:
        auto_off(data)

    if request.method == "POST":
        # User Reset
        if 'reset' in request.POST:
            data.active = False
            data.save()
            return render(request, 'brb/index.html', {
                "user": user,
                "time": current_time,
                "status": data.active,
            })
        # User Post request
        else:
            reason = request.POST["reason"]
            hours = request.POST["hour"]
            minutes = request.POST["minute"]

            if not hours:
                hours = 0
            else:
                hours = int(hours)
            if not minutes:
                minutes = 0
            else:
                minutes = int(minutes)

            if hours >= 0 and hours < 24 and minutes >= 0 and minutes < 60:
                data.reason = reason
                data.return_time = current_time + \
                    timedelta(hours=hours, minutes=minutes)
                data.active = True
                data.creation_time = current_time
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
                    "status": data.active,
                })
    # GET requests
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


""" # Dont need Register at this moment
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
"""


def superuser_view(request):
    UserModel = get_user_model()
    load_dotenv()

    print("Running Superuser check")
    if not UserModel.objects.filter(username=os.getenv("SUPERUSER_USER")).exists():
        user = UserModel.objects.create_user(
            os.getenv("SUPERUSER_USER"), password=os.getenv("SUPERUSER_PASSWORD"))
        user.is_superuser = True
        user.is_staff = True
        user.save()

    return HttpResponse(None)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def api(request):

    if Away.objects.all()[0]:
        away = Away.objects.all()[0]
        # Check if there user has forgotten to remove Away-status
        if away.active:
            auto_off(away)
    else:
        return HttpResponse("Error, no object found")

    if request.method == 'GET':
        # Active Status
        if away.active:
            serializer = AwaySerializer(away, many=False)
            return JsonResponse(serializer.data, safe=False)
        # No active Status
        else:
            return HttpResponse(None)
