from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

class AddTransaction(models.Model):
    current_balance = models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    Type  = [('Credit','Credit'),('Debit','Debit')]
    select_type = models.CharField(max_length=6,choices=Type)
    enter_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
