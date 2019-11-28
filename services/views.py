from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from services.forms import ReviewForm


# Create your views here.

# def services(request):
#     context = {}
#
#     form = ReviewForm(request.POST)
#
#     context['form'] = form
#     return render(request, 'services/services.html', context)


class ServicesView(TemplateView):
    template_name = 'services/services.html'

    def get(self, request, **kwargs):
        # form = ReviewForm()
        # context = {'form': form, 'first_image': Photo.objects.first(), 'images': Photo.objects.all()[1:12]}
        context = {}

        form = ReviewForm()

        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for Your Review')
            return redirect(reverse('services-home'))

        args = {'form': form}
        return render(request, self.template_name, args)
