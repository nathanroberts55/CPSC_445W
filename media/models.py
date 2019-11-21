from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Photo(models.Model):
    description = models.CharField(_('Photo Description'), max_length=45, default="")
    instagram_link = models.URLField(_('Instagram Link'), max_length=300, default="", blank=True)
    date_added = models.DateTimeField(auto_now=True)
    image = models.ImageField(_('Image File'), upload_to='gallery_images', default="", blank=False)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-date_added']
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')


class Video(models.Model):
    # description = models.CharField(_('Video Description'), max_length=45, default="")
    video_src = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')
        ordering = ['-date_added']


class Media(models.Model):
    photo_FK = models.ForeignKey(Photo, on_delete=models.CASCADE)
    video_FK = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')
