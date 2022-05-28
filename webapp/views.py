from .models import Event, BannerMessage
import datetime
from django.shortcuts import render

current_time = datetime.datetime.now()


def index(request):
    context = {}
    try:
        banner_message = BannerMessage.objects.all().filter(is_active=1)[:1][0]
        context['banner_message'] = banner_message
    except:
        banner_message = 'Unable to fetch message'

    events = Event.objects.all().filter(is_active=1).filter(
        start_date__gt=current_time).order_by('start_date')[:4]

    context['events'] = events
    return render(request, 'webapp/index.html', context)


def contact(request):
    context = {
        'title': 'Contact page',
    }
    return render(request, 'webapp/contact.html', context)


def services(request):
    context = {
        'title': 'Services page',
    }
    return render(request, 'webapp/services.html', context)


def training(request):
    context = {
        'title': 'training page',
    }
    return render(request, 'webapp/training.html', context)


def hr_life_cycle(request):
    context = {
        'title': 'hr-life-cycle page',
    }
    return render(request, 'webapp/hr-life-cycle.html', context)


def outsourcing(request):
    context = {
        'title': 'outsourcing page',
    }
    return render(request, 'webapp/outsourcing.html', context)


def recruitment(request):
    context = {
        'title': 'recruitment page',
    }
    return render(request, 'webapp/recruitment.html', context)


def african_talent(request):
    context = {
        'title': 'African talent page',
    }
    return render(request, 'webapp/african-talent.html', context)
