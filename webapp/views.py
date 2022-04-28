from django.shortcuts import render

from .models import Event


def index(request):
    events = Event.objects.all().order_by('start_date')[:4]
    context = {'events': events}
    return render(request, 'webapp/index.html', context)
