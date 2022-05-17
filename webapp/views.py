from .models import Event, BannerMessage
import datetime
from django.shortcuts import render

current_time = datetime.datetime.now()


def index(request):
    try:
        banner_message = BannerMessage.objects.all().filter(is_active=1)[:1][0]
    except:
        banner_message = False

    events = Event.objects.all().filter(is_active=1).filter(
        start_date__gt=current_time).order_by('start_date')[:4]
    context = {
        'events': events,
        'banner_message': banner_message
    }
    return render(request, 'webapp/index.html', context)
