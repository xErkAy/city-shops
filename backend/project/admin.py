from django.contrib import admin
from project.models import User
from api.models import City, Street, Shop

admin.site.register(User)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Shop)
