from django.contrib import admin
from .models import Profile, Message, Reply


# Register your models here.
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Reply)
