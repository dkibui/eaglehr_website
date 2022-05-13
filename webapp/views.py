from .models import Event
import datetime
from django.shortcuts import render

current_time = datetime.datetime.now()
print(current_time)


def index(request):
    events = Event.objects.all().filter(is_active=1).filter(
        start_date__gt=current_time).order_by('start_date')[:4]
    context = {'events': events}
    return render(request, 'webapp/index.html', context)
