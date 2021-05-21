from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import reverse
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from . import forms


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


class UserList(generic.ListView):
    model = User
    allow_empty = False


class CreateUser(generic.CreateView):
    model = User
    # fields = ['first_name', 'last_name', 'username', 'password']
    form_class = forms.CustomRegisterForm
    # context_object_name = "user_form"
    # success_url = reverse_lazy("cvbs:user_list")
    initial = {
        'first_name': "milad"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_success_url(self):
        return reverse("cvbs:user_detail", args=[self.object.id])


class UserDetail(generic.DetailView):
    model = User
