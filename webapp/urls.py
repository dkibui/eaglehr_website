from django.urls import path

from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("hr-life-cycle/", views.hr_life_cycle, name="hr-life-cycle"),
    path("outsourcing/", views.outsourcing, name="outsourcing"),
    path("recruitment/", views.recruitment, name="recruitment"),
    path("african-talent/", views.african_talent, name="african-talent"),
    path("events/<int:id>/", views.event, name="event"),
]
