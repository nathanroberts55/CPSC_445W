from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import *


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, editable=False)
    first_name = models.CharField(_('First Name'), max_length=ServicesConstants.CHAR_MAX_LENGTH, default="")
    last_name = models.CharField(_('Last Name'), max_length=ServicesConstants.CHAR_MAX_LENGTH, default="")
    review = models.TextField(_('Review'), max_length=5000, default="", blank=False)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
