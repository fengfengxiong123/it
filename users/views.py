from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


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
