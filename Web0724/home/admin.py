from django.contrib import admin
from .models import User
# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display = ('account_number','name','gender','email','password','createdate')

admin.site.register(User,Useradmin)