from django.urls import path, re_path
from django.contrib.auth.views import LoginView
from users.views import LogoutView, RegisterView,AccountView

app_name = 'users'
urlpatterns = [
    re_path(r'^login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^register/$', RegisterView.as_view(), name='register'),
    re_path(r'^account/$', AccountView.as_view(), name='account'),
]
