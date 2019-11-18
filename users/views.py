from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import unicodedata
from django import forms
from .models import User
from share.models import Dot


class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize('NFKC', super().to_python(value))


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('share:index'))


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('share:index'))
        context = {'form': form}
        return render(request, 'users/register.html', context)


class AccountView(View):
    def get(self, request):
        auth_user_id = request.session.get('_auth_user_id')
        user_obj = User.objects.get(id=auth_user_id)
        user_dots_query = Dot.objects.filter(user_id=auth_user_id).values('id', 'question', 'date_time_first')

        context = {'user_obj': user_obj, 'user_dots_query': user_dots_query}
        return render(request, 'users/account.html', context)
