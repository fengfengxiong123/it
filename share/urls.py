from django.urls import path,include,re_path
from . import views

urlpatterns = [

    path('',views.IndexView.as_view(),name='index'),
    path('add_dot/',views.AddDotView.as_view(),name='add_dot'),
    re_path(r'^dot/(?P<id>\d+)/$',views.DotView.as_view(),name='dot'),

]
