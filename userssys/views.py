from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm



def login(request):
    args ={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/polls/')
        else:
            args['login_error'] = "Аккаунт не знайдено"
            return render(request,'userssys/login.html',args)
    else:
        return render(request,'userssys/login.html',args)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/polls/')

def register(request):
    args ={}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],password=newuser_form.cleaned_data['password1'])
            auth.login(request,newuser)
            return HttpResponseRedirect('/polls/')
        else:
            args['form'] = newuser_form
    return render(request,'userssys/register.html',args)


