from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
