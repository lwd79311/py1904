from . import views
from django.conf.urls import url
app_name = "vote"

urlpatterns = [
    url(r'^index/$', views.index,name='index'),

]