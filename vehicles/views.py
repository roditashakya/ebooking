from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

# Create your views here.
from vehicles import models
from vehicles.forms import SignupForm, SigninForm
from vehicles.models import Search, Vehicle, BookingUser


def home(req):
    bus = Vehicle.objects.filter(name__contains=True)
    passenger = BookingUser.objects.filter(email__contains=True)
    context = {"bus": bus, "passenger": passenger}
    return render(req, "vehicles/home.html", context)
    #return HttpResponse("Hello World")

def list(req):
    traveldetails =models.TravelDetail.objects.all()
    context = {"traveldetails": traveldetails, "hello": "there"}
    return render(req, "vehicles/home.html", context)

def detail(req, id):
    traveldetail = models.TravelDetail.objects.all()
    # question = models.Search.objects.get(id=id)
    dict = {"traveldetail": traveldetail}
    return render(req, "vehicles/detail.html", dict)

def search(req):
    q = req.GET["q"]
    datas = Search.objects.filter(from_address=True, to_address__contains=q)
    return render(req, "vehicles/detail.html", {"datas": datas})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User Saved")
            redirect("vehicles/signin.html")
        else:
            messages.error(request, "Error in form")
    else:
        form = SignupForm()
    return render(request, "vehicles/signup.html", {"form": form})


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("/")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    context = {"form": form}
    return render(request, "vehicles/signin.html", context)



def signout(request):
    logout(request)
    return redirect("/signin")

def checkout(request):
    request.session.pop('data', None)
    return redirect("/")

def profile(req):
    return render(req, "vehicles/profile.html")

def googlemap(req):
    return render(req, "vehicles/map.html", {})

# def password_reset(request):
#     if request.method == "POST":
#         form = PasswordResetForm(request.POST)
#         return render(request, "vehicles/password_reset_done.html", {"form": form})
#
#     else:
#         form = PasswordResetForm(request.GET)
#     return render(request, "vehicles/password_reset.html", {"form": form})

# def add_schedule(req, id):
#     if req.method="POST":
#         form = ScheduleForm(req.POST)
#         if form.is_valid():
#             schedule = form.save(commit=False)
#             schedule.save()
#             seat_names = schedule.vehicle.seat_template.seat_name.split(",")
#             seat_prices = schedule.vehicle.seat_template.seat_name.split(",")
#
#             for index, seat in enumerate(seat_names):
#                 s = Seat()
#                 s.schedule = schedule
#                 s.name = seat
#                 s.price = seat_prices[index]
#                 s.save()
#             return redirect()
#     else:
#     form = ScheduleForm()
#     return render(req,"vehicles/add_schedule.html", {"form": form})