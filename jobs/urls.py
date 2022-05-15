from django.contrib import admin
from django.urls import path
from . import views

app_name = "jobs"
urlpatterns = [
    path('', views.job_list, name="jobs-list"),
    path('apply/<int:id>', views.apply_job_view, name="apply-job"),
    # path('apply/<int:id>', views.post_list_tag_filter, name="blog-list-tag"),
    path('<slug:slug>', views.job_detail, name="job-detail"),
]
