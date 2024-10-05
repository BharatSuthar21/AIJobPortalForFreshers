from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
from student.models import *


# CompanyDetails model
class CompanyDetails(models.Model):
    userId = models.ForeignKey(Users,on_delete=models.CASCADE)
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255)
    address = models.TextField()
    industryType = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.companyName


# JobDetails model
class JobDetails(models.Model):
    companyId = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    jobId = models.AutoField(primary_key=True)
    description = models.TextField()
    skills = models.TextField()
    payRange = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=50)
    field = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    expiryDate = models.DateField()
    postedOn = models.DateTimeField(auto_now_add=True)
    student_applied = models.JSONField(default=dict)
    def __str__(self):
        return f"Job {self.jobId} at {self.companyId}"


# InternshipDetails model
class InternshipDetails(models.Model):
    companyId = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    internshipId = models.AutoField(primary_key=True)
    description = models.TextField()
    skills = models.TextField()
    location = models.CharField(max_length=255)
    field = models.CharField(max_length=25)
    category = models.CharField(max_length=255)
    expiryDate = models.DateField()
    stipend = models.CharField(max_length=100, blank=True, null=True)
    duration = models.CharField(max_length=50)  # Duration of the internship
    postedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Internship {self.internshipId} at {self.companyId}"



class ContestDetails(models.Model):
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    contestUrl = models.URLField()

    def __str__(self):
        return self.title


class NewsDetails(models.Model):
    headline = models.CharField(max_length=255)
    summary = models.TextField()
    news_url = models.URLField()

    def __str__(self):
        return self.headline
    


class CompanyDashboard(models.Model):
    company = models.OneToOneField(CompanyDetails, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(JobDetails, blank=True)
    internships = models.ManyToManyField(InternshipDetails, blank=True)

    def __str__(self):
        return f"{self.company.company_name}'s Dashboard"
    
class JobApplication(models.Model):
    jobApplicationId = models.AutoField(primary_key=True)
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNumber = models.BigIntegerField()
    resume = models.FileField(upload_to='applications/')
    relevantWorkExperience = models.IntegerField()  # Assuming this is in months or years
    experienceCompanyName = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}'s Application for {self.job.description}"