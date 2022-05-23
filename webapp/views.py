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


def services(request):
    context = {
        'title': 'Services page',
    }
    return render(request, 'webapp/services.html', context)
