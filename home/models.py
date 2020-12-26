from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(_('Email'))
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
