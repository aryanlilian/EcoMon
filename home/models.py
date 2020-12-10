from django.db import models
from users.models import User

class Newsletter(models.Model):
    email = models.EmailField()
    subscribed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
