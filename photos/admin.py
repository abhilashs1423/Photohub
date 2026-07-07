from django.contrib import admin
from .models import Photographer, Photo, Booking

admin.site.register(Photographer)
admin.site.register(Photo)
admin.site.register(Booking)