from django.contrib import admin

from.models import carinfo
from .models import UserData, stationMapping

@admin.register(UserData)
class UserDetails(admin.ModelAdmin):
    list_display = ['username','email','password']

@admin.register(carinfo)
class Carlist(admin.ModelAdmin):
    list_display = ['carnumber', 'carstartlocation','carsecondlocation','carthridlocation','carfourthlocation','carendlocation','availableSeatsStop4', 'carstatus']

@admin.register(stationMapping)
class stationMappingDetails(admin.ModelAdmin):
    list_display = ['carnumber','runningdays','startLocation','nextLocation','availSeat','totalSeat','active']

