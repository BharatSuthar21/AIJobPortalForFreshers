from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    company_name = models.CharField(max_length=1000)
    skills = models.CharField(max_length=10000)
    posted_date = models.CharField(max_length=1000, null=True)
    apply_link = models.URLField()


class Internship(models.Model):
    company_name = models.CharField(max_length=1000)
    skills = models.CharField(max_length=10000)
    posted_date = models.CharField(max_length=1000, null=True)
    apply_link = models.URLField()


class Contest(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=1000)
    link = models.URLField()


class News(models.Model):
    # If with news we can also add like and dislike button so that users can validae the machine learning model.
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_patment_signature = models.CharField(max_length=100, null=True, blank=True)
    headline = models.CharField(max_length=1000)
    summary = models.CharField(max_length=10000000)
    link = models.URLField()
    percent = models.IntegerField()


class Contact(models.Model):
    q_name = models.CharField(max_length=100)
    q_email = models.EmailField()
    q_subject = models.CharField(max_length=1000)
    q_message = models.CharField(max_length=10000000)


