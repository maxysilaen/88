import requests
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.http.response import HttpResponseRedirect

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("my-tasks")
    return render(request, "form.html", {"form":form, "title": title})

class UserCreateView(TemplateResponseMixin, View):
    template_name = "accounts/form_register.html"
    form = UserRegisterForm

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'form': self.form,
                                        'title':"Register"
                                        })

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        email2 = request.POST.get('email2')
        password = request.POST.get('password')
        url = "http://localhost:8001/api/accounts/register/"
        payload = {'username':username, 'email':email,
                   'email2':email2, 'password':password}
        r = requests.post(url, data=payload)
        try:
            res_json = r.json()
            print res_json
            if r.status_code == 400:
                messages.add_message(request, messages.ERROR,
                                     res_json)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            elif r.status_code == 201:
                new_user = authenticate(username=username, password=password)
                login(request, new_user)
                return redirect('my-tasks')

        except:
            print r.text
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # {"username": "maya", "email": "mayakristi@gmail.com", "email2": "mayakristi@gmail.com"}
        # {u'username': [u'A user with that username already exists.'], u'password': [u'This field may not be blank.'],
        #  u'email2': [u'This field may not be blank.'], u'email': [u'Emails must match.']}


def logout_view(request):
    logout(request)
    return redirect("login")