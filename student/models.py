from django.db import models
from company.models import *
from accounts.models import *

class StudentDetails(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=50)
    studentEmail = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    phoneNumner = models.BigIntegerField(len=10)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    cgpa = models.FloatField(max_length=4)
    internshipDone = models.BooleanField(default=False)
    internshipData = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')  # Upload resume
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    open_source = models.BooleanField(default=False)
    open_source_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.studentName

class UserApplications(models.Model):
    user = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    job = models.ForeignKey(JobDetails, on_delete=models.CASCADE, blank=True, null=True)
    internship = models.ForeignKey(InternshipDetails, on_delete=models.CASCADE, blank=True, null=True)
    contest = models.ForeignKey(ContestDetails, on_delete=models.CASCADE, blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.job:
            return f'{self.user.full_name} applied for {self.job.title}'
        elif self.internship:
            return f'{self.user.full_name} applied for {self.internship.title}'
        return f'{self.user.full_name} applied for {self.contest.name}'

class StudentDashboard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    jobs_applied = models.JSONField(default=dict)  # Use JSONField to store hashmap-like data
    internships_applied = models.JSONField(default=dict)  # Use JSONField to store hashmap-like data

    def __str__(self):
        return f"{self.student.student_name}'s Dashboard"

class JobTracking(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('sent', 'Sent to Company'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('interview', 'Interview Scheduled'),
        ('selected', 'Selected'),
        ('not_selected', 'Not Selected'),
    ]
    
    user_application = models.ForeignKey(UserApplications, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    last_updated = models.DateTimeField(auto_now=True)
    interview_or_exam_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.user_application} is {self.get_status_display()}'

class StudentBookmark(models.Model):
    bookmarkId = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    jobs = models.ManyToManyField(JobDetails, blank=True)
    internships = models.ManyToManyField(InternshipDetails, blank=True)
    bookmarkDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark for {self.student.student_name} on {self.bookmark_date}"

class Notification(models.Model):
    user = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.full_name}'
