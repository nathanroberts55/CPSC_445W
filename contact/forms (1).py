from django import forms
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.utils.translation import ugettext_lazy as _

from nr_media import settings
from .models import Client


class ClientContactForm(forms.ModelForm):
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'id': 'subject', 'placeholder': _('Subject')
        }
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control', 'id': 'message', 'placeholder': _('A little idea of what you want to do...')
        }
    ))

    def clean_zip_code(self):
        if len(self.cleaned_data['zip_code']) > 5:
            raise ValidationError(_('Zip code cannot be longer than 5 digits. Please re-enter the value.'))
        return self.cleaned_data['zip_code']

    def clean_first_name(self):
        if self.cleaned_data['first_name'].isdigit():
            raise ValidationError(_('First Name should ONLY contain characters'))
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if self.cleaned_data['last_name'].isdigit():
            raise ValidationError(_('Last Name should ONLY contain characters'))
        return self.cleaned_data['last_name']

    def save(self, commit=True, **kwargs):
        client = super().save(commit=False)
        if commit:
            client.save()
            mail_subject = self.cleaned_data['subject']
            mail_message = self.cleaned_data['message']
            mail_city = self.cleaned_data['city']
            mail_state = self.cleaned_data['state']
            mail_zip = self.cleaned_data['zip_code']
            form_email = self.cleaned_data['email']  # email client submitted
            form_first_name = self.cleaned_data['first_name']
            form_last_name = self.cleaned_data['last_name']
            text = get_template('emails/txt/signup_email.txt')
            htmly = get_template('emails/html/signup_email.html')
            context = {  # pass variables into templates
                'email': form_email,
                'message': mail_message,
                'subject': mail_subject,
                'first_name': form_first_name,
                'last_name': form_last_name,
                'city': mail_city,
                'state': mail_state,
                'zip_code': mail_zip,
            }
            text_content = text.render(context)
            html_content = htmly.render(context)
            message = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER,
                                             [settings.EMAIL_HOST_USER])
            message.attach_alternative(html_content, 'text/html')
            message.send()

    class Meta:

        model = Client
        fields = ['first_name', 'last_name', 'email', 'city', 'state', 'zip_code']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'FName', 'placeholder': _('First Name')}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'LName', 'placeholder': _('Last Name')}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'id': 'id', 'placeholder': _('Example@example.com')}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('City')}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Zip Code')}),
        }
