from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.auth import logout, authenticate, login
from .admin import MyUserCreationForm
from django.http import HttpResponseRedirect
from .models import MyUser
from share.models import Dot


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('share:index'))


class RegisterView(View):
    def get(self, request):
        form = MyUserCreationForm()
        context = {'form': form}
        print(context)
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(data=request.POST)
        print(request.POST)
        if form.is_valid():
            print('111')
            new_user = form.save()
            authenticated_user = authenticate(username=new_user, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('share:index'))
        context = {'form': form}
        return render(request, 'users/register.html', context)


class AccountView(View):
    def get(self, request):
        auth_user_id = request.session.get('_auth_user_id')
        user_obj = MyUser.objects.get(id=auth_user_id)
        user_dots_query = Dot.objects.filter(user_id=auth_user_id).values('id', 'question', 'date_time_first')

        context = {'user_obj': user_obj, 'user_dots_query': user_dots_query}
        return render(request, 'users/account.html', context)
