from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Info(models.Model):
    title = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('cbvs:info_detail', args=[self.id])

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class Child(models.Model):
    title = models.ForeignKey(to=Info, null=True, on_delete=models.CASCADE)
