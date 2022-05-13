from django import forms
from .models import Post, Application


class ApplicationForm(forms.ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    resume = forms.FileField(widget=forms.FileInput(attrs={'class': 'file'}))

    first_name = forms.CharField(widget=forms.TextInput, error_messages={
        'required': 'Your first name is required'})
    last_name = forms.CharField(widget=forms.TextInput, error_messages={
        'required': 'Your last name is required'})
    email = forms.CharField(widget=forms.TextInput, error_messages={
        'required': 'Your email is required'})
    phone = forms.CharField(widget=forms.TextInput, error_messages={
        'required': 'Your phone number is required'})
    cover_letter = forms.FileField(widget=forms.FileInput, error_messages={
        'required': 'You must select your cover letter'})
    resume = forms.FileField(widget=forms.FileInput, error_messages={
        'required': 'You must select your resume'})
    # reference = forms.CharField(widget=forms.TextInput, error_messages={
    #     'required': 'You must fill your reference'})

    class Meta:
        model = Application
        fields = ("first_name", "last_name", "email",
                  "phone", "reference", "cover_letter", "resume", )

        labels = {
            'first_name': 'Your first name',
            'reference': 'How did you hear about this is job?',
        }

        error_messages = {
            'first_name': {
                'max_length': "Your first name is too long.",
                'min_length': "Your first name is too short.",
            },
        }
