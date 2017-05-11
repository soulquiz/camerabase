from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^live_steam/$', views.live_steam, name='live_steam'),
    url(r'^setting_mode/$', views.setting_mode, name='setting_mode'),
]
