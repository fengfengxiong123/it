from django.urls import path, include, re_path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'share'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_dot/', login_required(views.AddDotView.as_view()), name='add_dot'),
    re_path(r'^dot/(?P<id>\d+)/$', views.DotView.as_view(), name='dot'),
]
