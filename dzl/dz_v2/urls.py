"""dz_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dz2 import views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^groups/$', views.groups_view.as_view()),
    url(r'^group/(?P<id1>\d+)$', views.group_view.as_view(), name='group_url'),
    url(r'^create_group/$', views.create_group.as_view()),
    url(r'^add/(?P<id2>\d+)$', views.add.as_view(), name='add_url'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns.append(url(r'$', views.groups_view.as_view()))
