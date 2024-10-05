from django.db import models

class Users(models.Model):
    userId = models.IntegerField(primary_key=True, default=1111)
    joiningDate = models.DateTimeField(auto_now_add=True)
    userType = models.BooleanField(default=False)