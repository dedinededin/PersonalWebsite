from django.shortcuts import render, redirect
from .models import Contact, Event, EventOwner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from mysite.cinema_controller import get_films


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        friends = profile.friends.all()
        owner = EventOwner.objects.filter(profile=request.user.profile)
        events = Event.objects.filter(owner__in=owner)
        context = {'home': 'active', 'friends': friends, 'events': events,
                   'name': profile.first_name + " " + profile.last_name}
        return render(request, 'mysite/index.html', context)
    else:
        context = {'home': 'active'}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        friends = profile.friends.all()
        owner_friends = EventOwner.objects.filter(profile__in=friends)
        events = Event.objects.filter(owner__in=owner_friends.all())

        context = {'portfolio': 'active', 'events': events}
        return render(request, 'mysite/portfolio.html', context)

    else:
        context = {'portfolio': 'active'}
        return render(request, 'mysite/portfolio.html', context)


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact(email=email, subject=subject, message=message)
        c.save()
        context = {'contact': 'active', 'message': 'We got your mail'}
        return render(request, 'mysite/contact.html', context)
    else:
        context = {'contact': 'active'}
        return render(request, 'mysite/contact.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def explore(request):
    films = get_films()
    context = {'explore': 'active', 'films': films}
    return render(request, 'mysite/explore.html', context)
