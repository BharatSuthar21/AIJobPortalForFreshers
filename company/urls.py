from django.urls import path
from company.Views.JobView import jobs;
from company.Views.InternshipView import internships;
from company.Views.CompanyView import manage_company;
from company.Views.ContestView import contests;
from company.Views.NewsView import news;
urlpatterns = [

    path('job/', jobs, name='job'),
    path('internship/', internships, name='internship'),
    path("contest/", contests, name='contest'),
    path("news/", news, name='news'),

    
    # Company-related endpoints
    path('companies/manage/', manage_company, name='manage_company'),
]
