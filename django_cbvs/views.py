from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


class UserList(generic.ListView):
    model = User
    # context_object_name = "users"
    queryset = User.objects.filter(username='test')
    allow_empty = False

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(UserList, self).get_context_data(**kwargs)
    #     context["test"] = User.objects.filter(username='User2')
    #     print(context)
    #     return context
