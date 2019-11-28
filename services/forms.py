from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Review


class ReviewForm(forms.ModelForm):

    def clean_first_name(self):
        if self.cleaned_data['first_name'].isdigit():
            raise ValidationError(_('First Name should ONLY contain characters'))
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if self.cleaned_data['last_name'].isdigit():
            raise ValidationError(_('Last Name should ONLY contain characters'))
        return self.cleaned_data['last_name']

    def save(self, commit=True, **kwargs):
        review = super().save(commit=False)
        if commit:
            review.save()

    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'review']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'FName', 'placeholder': _('First Name')}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'LName', 'placeholder': _('Last Name')}),
            'review': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'Review', 'rows': 5,
                       'placeholder': _('Leave a Review of Your Experience')}),
        }
