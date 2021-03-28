from django.db import models
from django.contrib.auth.models import User
class Members(models.Model):
	society_id = models.ForeignKey(User,on_delete=models.CASCADE)
	wing = models.CharField(max_length=3)
	flat_no = models.PositiveIntegerField()
	owner = models.CharField(max_length=50)
	contact = models.CharField(max_length=13)
	parking = models.CharField(max_length=10)
	status = models.IntegerField(choices=[(0,'Self'),(1,'Rented')])