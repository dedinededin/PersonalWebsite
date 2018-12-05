from django.contrib import admin
from .models import Profile,Contact,Event,EventOwner

from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Profile)
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(EventOwner)