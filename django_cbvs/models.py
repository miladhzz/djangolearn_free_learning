from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Info(models.Model):
    title = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('cvbs:info_detail', args=[self.id])
