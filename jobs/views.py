from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import ApplicationForm
from .models import Post
from datetime import date

# import phonenumbers
# from phonenumbers import timezone

current_year = date.today().year


per_page = 10
count = 0


def job_list(request):
    query = request.GET.get("query")
    context = {
        "title": f"Sharing sought after python and django tips and tricks for web development. Here to help you upskill your web development in {current_year}"
    }
    posts = Post.objects.all().filter(active=1)

    paginator = Paginator(posts, per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context["page_obj"] = page_obj
    context["count"] = len(list(posts))

    return render(request, "jobs/index.html", context)


def post_list_tag_filter(request, tag_slug=None):
    posts = Post.objects.all().filter(active=1)
    context = {
        "title": f"Upto date python and django jobs articles to upskill your web development skills in {current_year}"
    }

    return render(request, "jobs/index.html", context)


def job_detail(request, slug):
    context = {}
    path = request.path
    host = request.get_host()
    print(host + path)
    try:
        job = Post.objects.get(slug=slug)
        context["job"] = job
    except:
        messages.error(request, f"This page is not available: {host+path}")
        return redirect("jobs:jobs-list")
    if job.active != 1:
        messages.error(request, f"{host+path} is currently not available")
        return redirect("jobs:jobs-list")
    return render(request, "jobs/job-detail.html", context)


def apply_job_view(request, id):
    job = Post.objects.get(pk=id)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Thank you, your application was submitted successfully"
            )
            return redirect("jobs:jobs-list")
        else:
            form = ApplicationForm(request.POST, request.FILES)
            context = {"form": form, "job": job}
            messages.error(request, f"Please fill all required fields")
            return render(request, "jobs/apply-job.html", context)

    else:
        print(job)
        form = ApplicationForm()
        context = {"form": form, "job": job}
        return render(request, "jobs/apply-job.html", context)
