from django.contrib import admin

# Register your models here.
from media.models import Photo, Video

admin.site.register(Photo)
admin.site.register(Video)
