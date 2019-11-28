from django.contrib.auth.models import User
from django.db import models

from .constants import *

admin = User.objects.first()


# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, editable=False)
    first_name = models.CharField(max_length=ContactConstants.CHAR_MAX_LENGTH)
    last_name = models.CharField(max_length=ContactConstants.CHAR_MAX_LENGTH)
    email = models.EmailField()
    city = models.CharField(max_length=ContactConstants.CHAR_MAX_LENGTH)
    state = models.CharField(max_length=100, choices=ContactConstants.STATE_ABBREVIATIONS)
    zip_code = models.CharField(max_length=6)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['first_name', 'last_name']  # order by first name and then last name
