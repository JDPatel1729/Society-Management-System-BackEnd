from django.db import models
from django.contrib.auth.models import User

class Ledger(models.Model):
	society_id = models.ForeignKey(User,on_delete=models.CASCADE)
	date_time = models.DateTimeField(auto_now_add=True)
	mode = models.IntegerField(choices=[(0,'Debit'),(1,'Credit')])
	amount = models.PositiveIntegerField()
	remark = models.CharField(max_length=150)