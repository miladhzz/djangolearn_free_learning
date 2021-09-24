from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import reverse
from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm
from . import forms
from . import models


@login_required
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
    # success_url = reverse_lazy("cbvs:user_list")
    initial = {
        'first_name': "milad"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def get_success_url(self):
        return reverse("cbvs:user_detail", args=[self.object.id])


class UserDetail(generic.DetailView):
    model = User


class UpdateUser(generic.UpdateView):
    model = User
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        return reverse("cbvs:user_detail", args=[self.object.id])


class InfoList(generic.ListView):
    model = models.Info


class InfoDetail(generic.DetailView):
    model = models.Info


class UpdateInfo(generic.UpdateView):
    model = models.Info
    fields = ['title']


class DeleteInfo(generic.DeleteView):
    model = models.Info
    success_url = reverse_lazy('cbvs:index')
    slug_url_kwarg = "title"
    slug_field = "title"

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        return models.Info.objects.filter(title=title)[0]

    def get_context_data(self, **kwargs):
        context = super(DeleteInfo, self).get_context_data(**kwargs)
        print(context)
        return context


@method_decorator(login_required, name='dispatch')
class TestDispatch(generic.View):
    def get(self, *args, **kwargs):
        return HttpResponse("<h1>Hello TestDispatch!</h1>")
