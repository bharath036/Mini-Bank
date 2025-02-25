from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    current_balance = models.FloatField(default=0)

    def __str__(self):
        return f"The current available is {self.current_balance}"

class AddTransaction(models.Model):
    current_balance = models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    Type  = [('Credit','Credit'),('Debit','Debit')]
    select_type = models.CharField(max_length=6,choices=Type)
    enter_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The amount is {self.enter_amount} {self.select_type}ed into your account"

class RequestLogs(models.Model):
    request_info = models.TextField()
    #GET,POST 
    request_type = models.CharField(max_length=100)
    #request method to store URL path
    request_method = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
