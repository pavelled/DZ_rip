from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.group, name='group'),
url(r'^$', views.group_user, name='group_user')
]