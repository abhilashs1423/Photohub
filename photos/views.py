from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages

def booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Booking Submitted Successfully!"
            )

            return redirect('/booking/')

    else:

        form = BookingForm()

    return render(
        request,
        'booking.html',
        {'form': form}
    )


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account Created Successfully!")

        return redirect('/login/')

    return render(request, 'register.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, "Login Successfully!")

            return redirect('/booking/')

        else:

            messages.error(
                request,
                "Invalid Username or Password"
            )

    return render(request, 'login.html')


def booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Booking Submitted Successfully!"
            )

    else:

        form = BookingForm()

    return render(
        request,
        'booking.html',
        {'form': form}
    )
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')


def gallery(request):
    return render(request, 'gallery.html')


def photographer(request):
    return render(request, 'photographer.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def user_logout(request):
    logout(request)
    return redirect('/')