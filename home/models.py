from django.db import models
from django.urls import reverse


class Newsletter(models.Model):
    email = models.EmailField()
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('index')
