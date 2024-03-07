from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class police_station(models.Model):
    stationname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)



class missing_details(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    id_proof = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default=1)
    POLICESTATION = models.ForeignKey(police_station,on_delete=models.CASCADE,default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class feedback(models.Model):
    feedbacks = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class admin_complaint(models.Model):
    complaints = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class police_complaint(models.Model):
    complaints = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    POLICESTATION = models.ForeignKey(police_station, on_delete=models.CASCADE, default=1)

class emergency(models.Model):
    name = models.CharField(max_length=100)
    emergency_contact = models.BigIntegerField()

class camera(models.Model):
    camera_no = models.CharField(max_length=100)
    POLICESTATION = models.ForeignKey(police_station, on_delete=models.CASCADE, default=1)

class category(models.Model):
    category_name = models.CharField(max_length=100)

class wanted_details(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    POLICESTATION = models.ForeignKey(police_station, on_delete=models.CASCADE, default=1)
    CATEGORY = models.ForeignKey(category, on_delete=models.CASCADE, default=1)


