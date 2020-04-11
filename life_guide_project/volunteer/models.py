from django.db import models
from datetime import datetime

# Create your models here.
class Volunteer(models.Model):
    Vol_id = models.AutoField(primary_key = True)
    date = models.DateField(default=datetime.now)
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")
    email = models.CharField(max_length=100,default="")
    location = models.CharField(max_length=100,default="")
    def __str__(self):
        return '%d %s %s' % (self.Vol_id, self.first_name, self.date)