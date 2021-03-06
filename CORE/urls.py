"""CORE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# ...........................................................
# default: "Django Administration"
admin.site.site_header = 'EAGLEHR CONSULTANTS'
# default: "Site administration"
admin.site.index_title = 'WELCOME TO EAGLEHR'
# default: "Django site admin"
admin.site.site_title = 'Eaglehr'
# ...........................................................


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls'), name='home_page'),
    path('jobs/', include('jobs.urls')),
    path('user/', include('User.urls')),
    path('blog/', include('blogs.urls')),
    path('news/', include('news.urls')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
