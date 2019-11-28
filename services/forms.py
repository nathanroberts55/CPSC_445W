from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Review


class ReviewForm(forms.ModelForm):
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
