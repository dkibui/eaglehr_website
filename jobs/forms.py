import phonenumbers
from phonenumbers import timezone
from django import forms
from .models import Post, Application
from .reference_choices import WAYS_TO_FIND_US


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
    reference = forms.ChoiceField(
        choices=WAYS_TO_FIND_US, label='Tell us how you found this job?',)

    class Meta:
        model = Application
        fields = ("first_name", "last_name", "email",
                  "phone", "reference", "cover_letter", "resume", )

    # def clean_phone(self, *args, **kwags):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone == '0728494090':
    #         raise forms.ValidationError('Please enter a valid phone number')
    #     return phone

        # parsed_phone_number = phonenumbers.parse(str(phone), 'KE')
        # if phonenumbers.is_valid_number(parsed_phone_number) == False:
        #     raise forms.ValidationError('Please enter a valid phone number')
        # return phone
