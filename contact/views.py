from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from contact.forms import ClientContactForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
from media.models import Photo


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    # def contact(request):
    #     context = {}
    #     form = ClientContact()
    #     context['form'] = form
    #     return render(request, template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  # generate default context data
    #     context['images'] = Photo.objects.all()[:12]
    #     print(context['images'])
    #     return context

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

        args = {'form': form}
        return render(request, self.template_name, args)
