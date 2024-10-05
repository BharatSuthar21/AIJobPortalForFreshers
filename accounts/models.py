from django.db import models

class Users(models.Model):
    userId = models.IntegerField(primary_key=True)
    joiningDate = models.DateTimeField(auto_now_add=True)
    userType = models.IntegerField(null=False)