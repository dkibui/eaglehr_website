from django import forms
from .models import Post, Application


class ApplicationForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'file'}))

    class Meta:
        model = Application
        fields = ("first_name", "last_name", "email",
                  "phone", "cover_letter", "resume", "reference")

        labels = {
            'first_name': 'Your first name',
            'reference': 'How did you hear about this is job?',
        }

        error_messages = {
            'first_name': {
                'max_length': "This writer's name is too long.",
            },
        }
