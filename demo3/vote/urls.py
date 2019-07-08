from . import views
from django.conf.urls import url
app_name = "vote"

urlpatterns = [
    url(r'^login/$',views.login,name="login"),
    url(r'^logout/$',views.logout,name="logout"),
    url(r'^$', views.index,name="index"),
    url(r'^list/(\d+)/$',views.list,name="list"),
    url(r'^result/(\d+)/$',views.result,name="result")
]