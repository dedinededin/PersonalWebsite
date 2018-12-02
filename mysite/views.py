from django.shortcuts import render
from .models import Contact


# Create your views here.

def index(request):
    context = {'home': 'active'}
    return render(request, 'mysite/index.html', context)


def portfolio(request):
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
