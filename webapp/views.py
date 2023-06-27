from .models import Event, BannerMessage, Event
from django.contrib import messages
import datetime
from django.shortcuts import render, redirect

current_time = datetime.datetime.now()


def test(request):
    return render(request, "webapp/jobs.html")


def index(request):
    context = {}
    try:
        banner_message = BannerMessage.objects.all().filter(is_active=1)[:1][0]
        context["banner_message"] = banner_message
    except Exception as e:
        banner_message = "Unable to fetch message"

    events = (
        Event.objects.all()
        .filter(is_active=1)
        .filter(start_date__gt=current_time)
        .order_by("start_date")[:3]
    )

    context["events"] = events
    return render(request, "webapp/index.html", context)


def contact(request):
    context = {
        "title": "Contact page",
    }
    return render(request, "webapp/contact.html", context)


def services(request):
    context = {
        "title": "Services page",
    }
    return render(request, "webapp/services.html", context)


def training(request):
    context = {
        "title": "training page",
    }
    return render(request, "webapp/training.html", context)


def hr_life_cycle(request):
    context = {
        "title": "hr-life-cycle page",
    }
    return render(request, "webapp/hr-life-cycle.html", context)


def outsourcing(request):
    context = {
        "title": "outsourcing page",
    }
    return render(request, "webapp/outsourcing.html", context)


def recruitment(request):
    context = {
        "title": "recruitment page",
    }
    return render(request, "webapp/recruitment.html", context)


def african_talent(request):
    context = {
        "title": "African talent page",
    }
    return render(request, "webapp/african-talent.html", context)


def event(request, id):
    context = {
        "title": "Eaglehr upcoming events",
    }
    events = Event.active_event.all()
    try:
        other_events = events.exclude(id=id)[:8]
        target_event = events.filter(id=id)
        context["other_events"] = other_events
        context["target_event"] = target_event
    except:
        messages.error(request, f"This event is not available")
        return redirect("webapp:index")

    return render(request, "webapp/event.html", context)
