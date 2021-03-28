from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
	society_id = models.ForeignKey(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	designation = models.CharField(max_length=30)
	contact = models.CharField(max_length=13)
	