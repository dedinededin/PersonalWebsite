from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('register', views.register, name='register'),
    path('explore', views.explore, name='explore'),

]
