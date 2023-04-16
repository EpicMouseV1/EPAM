from django.contrib import admin
from .models import Client, Brigade, Operator, Request
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

admin.site.register(MyUser)

admin.site.register(Client)
admin.site.register(Brigade)
admin.site.register(Operator)
admin.site.register(Request)
