from django.shortcuts import render
from media.models import Photo
from django.http import HttpResponse


# Create your views here.


def media(request):
    # want to get most recent x pictures
    context = {}

    first_x_photos = Photo.objects.all()[:12]  # first 12 queried items
    #  [0 1 2 4 5 6 7 8 9 10 11]

    context['first_three'] = first_x_photos[:3]  # [0 1 2] first three elements
    context['second_three'] = first_x_photos[3:6]  # [3 4 5]
    context['third_three'] = first_x_photos[6:9]  # [6 7 8]
    context['fourth_three'] = first_x_photos[9:12]

    return render(request, 'media/media.html', context)
