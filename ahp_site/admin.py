from django.contrib import admin
from .models import Report, Vehicle, Comment

# Register your models here.

admin.site.register(Report)
admin.site.register(Comment)
admin.site.register(Vehicle)
