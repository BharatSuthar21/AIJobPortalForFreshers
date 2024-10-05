from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
import datetime

# CompanyDetails model
class companyDetails(models.Model):
    userId = models.ForeignKey(Users, on_delete=models.CASCADE, default=1111)  # Default to user with ID 1
    companyId = models.AutoField(primary_key=True)
    companyName = models.CharField(max_length=255, default="Unknown Company")  # Default company name
    address = models.TextField(default="No address provided")  # Default address
    industryType = models.CharField(max_length=100, default="Unknown Industry")  # Default industry
    phoneNumber = models.CharField(max_length=20, default="1234567890")
    email = models.EmailField(max_length=255, unique=True, default="company@example.com")  # Default email
    website = models.URLField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    sector = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.companyName


# JobDetails model
class jobDetails(models.Model):
    companyId = models.ForeignKey(companyDetails, on_delete=models.CASCADE)
    jobId = models.AutoField(primary_key=True)
    description = models.TextField(default="No description provided")  # Default job description
    skills = models.TextField(default="No skills required")  # Default skills
    payRange = models.CharField(max_length=100, default="Not specified")  # Default pay range
    location = models.CharField(max_length=255, default="Remote")  # Default location
    duration = models.CharField(max_length=50, default="Permanent")  # Default duration
    field = models.CharField(max_length=25, default="General")  # Default field
    category = models.CharField(max_length=25, default="Full-time")  # Default category
    expiryDate = models.DateField(default=datetime.date.today)
    postedOn = models.DateTimeField(auto_now_add=True)
    student_applied = models.JSONField(default=dict)  # Default empty dictionary for applied students

    def __str__(self):
        return f"Job {self.jobId} at {self.companyId}"


# InternshipDetails model
class internshipDetails(models.Model):
    companyId = models.ForeignKey(companyDetails, on_delete=models.CASCADE)
    internshipId = models.AutoField(primary_key=True)
    description = models.TextField(default="No description provided")  # Default internship description
    skills = models.TextField(default="No skills required")  # Default skills
    location = models.CharField(max_length=255, default="Remote")  # Default location
    field = models.CharField(max_length=25, default="General")  # Default field
    category = models.CharField(max_length=255, default="Full-time")  # Default category
    expiryDate = models.DateField(default=datetime.date.today)
    stipend = models.CharField(max_length=100,  default="Unpaid")  # Default stipend
    duration = models.CharField(max_length=50, default="3 months")  # Default internship duration
    postedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Internship {self.internshipId} at {self.companyId}"


class contestDetails(models.Model):
    company = models.ForeignKey(companyDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="Untitled Contest")  # Default contest title
    contestUrl = models.URLField(default="http://example.com")  # Default contest URL

    def __str__(self):
        return self.title


class newsDetails(models.Model):
    headline = models.CharField(max_length=255, default="Untitled Headline")  # Default headline
    summary = models.TextField(default="No summary available")  # Default summary
    news_url = models.URLField(default="http://example.com")  # Default news URL

    def __str__(self):
        return self.headline


class companyDashboard(models.Model):
    company = models.OneToOneField(companyDetails, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(jobDetails, blank=True)
    internships = models.ManyToManyField(internshipDetails, blank=True)

    def __str__(self):
        return f"{self.company.companyName}'s Dashboard"


class jobApplication(models.Model):
    jobApplicationId = models.AutoField(primary_key=True)
    job = models.ForeignKey(jobDetails, on_delete=models.CASCADE)
    student = models.ForeignKey('student.studentDetails', on_delete=models.CASCADE)  # String reference to avoid circular import
    name = models.CharField(max_length=255, default="Unknown Applicant")  # Default applicant name
    email = models.EmailField(default="applicant@example.com")  # Default email
    phoneNumber = models.BigIntegerField(default=1234567890)  # Default phone number
    resume = models.FileField(upload_to='applications/', default='applications/default_resume.pdf')  # Default resume file
    relevantWorkExperience = models.IntegerField(default=0)  # Default work experience (0 years)
    experienceCompanyName = models.CharField(max_length=255, default="No experience")  # Default experience company name

    def __str__(self):
        return f"{self.name}'s Application for {self.job.description}"
