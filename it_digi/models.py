from django.db import models
class UserData(models.Model):
    #name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    #contact=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class carinfo(models.Model):
    carnumber=models.CharField(max_length=20)
    # carstarttime=models.DateTimeField()
    # carendtime=models.DateTimeField()
    runningdays = models.CharField(max_length=30)
    # seats = models.IntegerField()
    carstartlocation=models.CharField(max_length=30)
    carsecondlocation = models.CharField(max_length=30)
    availableSeatsStop1 = models.IntegerField(default=0)
    carthridlocation = models.CharField(max_length=30)
    availableSeatsStop2 = models.IntegerField(default=0)
    carfourthlocation = models.CharField(max_length=30)
    availableSeatsStop3 = models.IntegerField(default=0)
    carendlocation = models.CharField(max_length=30)
    availableSeatsStop4 = models.IntegerField(default=0)
    carstatus = models.CharField(max_length=30)

class stationMapping(models.Model):
    carnumber = models.CharField(max_length=20)
    runningdays = models.CharField(max_length=30)
    startLocation = models.CharField(max_length=30)
    nextLocation = models.CharField(max_length=30)
    availSeat = models.IntegerField()
    totalSeat = models.IntegerField()
    active = models.CharField(max_length=20)





