from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from contact.forms import ClientContactForm
# Create your views here.
from media.models import Photo


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get(self, request, **kwargs):
        form = ClientContactForm()
        context = {'form': form, 'first_image': Photo.objects.first(), 'images': Photo.objects.all()[1:12]}
        return render(request, self.template_name, context)

    def post(self, request):
        form = ClientContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for signing up!')
            return redirect(reverse('contact-home'))

        context = {'form': form, 'first_image': Photo.objects.first(), 'images': Photo.objects.all()[1:12]}
        return render(request, self.template_name, context)
