from django.db import models
from company.models import *
from accounts.models import *


class studentDetails(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=11111)  # Default to user with ID 1
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=50, default="Unknown Student")  # Default student name
    studentEmail = models.EmailField(default="example@example.com")  # Default email
    bio = models.TextField(blank=True, null=True)
    phoneNumber = models.BigIntegerField(null=False, default=1234567890)  # Default phone number
    college = models.CharField(max_length=50, default="Unknown College")  # Default college
    branch = models.CharField(max_length=50, default="Unknown Branch")  # Default branch
    cgpa = models.FloatField(max_length=4, default=0.0)  # Default CGPA
    internshipDone = models.BooleanField(default=False)
    internshipData = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', default='resumes/default_resume.pdf')  # Default resume file
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    open_source = models.BooleanField(default=False)
    open_source_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.studentName


class studentDashboard(models.Model):
    student = models.OneToOneField(studentDetails, on_delete=models.CASCADE)
    jobs_applied = models.JSONField(default=dict)  # Default to empty dict
    internships_applied = models.JSONField(default=dict)  # Default to empty dict

    def __str__(self):
        return f"{self.student.studentName}'s Dashboard"


class jobTracking(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('sent', 'Sent to Company'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('interview', 'Interview Scheduled'),
        ('selected', 'Selected'),
        ('not_selected', 'Not Selected'),
    ]
    
    user_application = models.ForeignKey(studentDashboard, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    last_updated = models.DateTimeField(auto_now=True)
    interview_or_exam_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user_application} is {self.get_status_display()}'


class studentBookmark(models.Model):
    bookmarkId = models.AutoField(primary_key=True)
    student = models.ForeignKey(studentDetails, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(jobDetails, blank=True)
    internships = models.ManyToManyField(internshipDetails, blank=True)
    bookmarkDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark for {self.student.studentName} on {self.bookmarkDate}"


class Notification(models.Model):
    user = models.ForeignKey(studentDetails, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, default="No message")  # Default message
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.studentName}'
