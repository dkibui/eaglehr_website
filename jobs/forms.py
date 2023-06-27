from django import forms
from .models import Post, Application
from .reference_choices import WAYS_TO_FIND_US


class ApplicationForm(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"

    resume = forms.FileField(widget=forms.FileInput(attrs={"class": "file"}))

    first_name = forms.CharField(
        widget=forms.TextInput,
        error_messages={"required": "Your first name is required"},
    )
    last_name = forms.CharField(
        widget=forms.TextInput,
        error_messages={"required": "Your last name is required"},
    )
    email = forms.CharField(
        widget=forms.TextInput, error_messages={"required": "Your email is required"}
    )
    phone = forms.CharField(
        widget=forms.TextInput,
        error_messages={"required": "Your phone number is required"},
    )
    cover_letter = forms.FileField(
        widget=forms.FileInput,
        error_messages={"required": "You must select your cover letter"},
    )
    resume = forms.FileField(
        widget=forms.FileInput,
        error_messages={"required": "You must select your resume"},
    )
    reference = forms.ChoiceField(
        choices=WAYS_TO_FIND_US,
        label="Tell us how you found this job?",
    )

    class Meta:
        model = Application
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone",
            "reference",
            "cover_letter",
            "resume",
        )

    # def clean_phone(self, *args, **kwags):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone == '0728494090':
    #         raise forms.ValidationError('Please enter a valid phone number')
    #     return phone

    # parsed_phone_number = phonenumbers.parse(str(phone), 'KE')
    # if phonenumbers.is_valid_number(parsed_phone_number) == False:
    #     raise forms.ValidationError('Please enter a valid phone number')
    # return phone

    def clean_first_name(self, *args, **kwags):
        first_name = self.cleaned_data.get("first_name")
        if len(first_name) < 2:
            raise forms.ValidationError("Name must be atleast 2 characters")
        if not first_name.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must be alpha characters")
        return first_name

    def clean_last_name(self, *args, **kwags):
        last_name = self.cleaned_data.get("last_name")
        if len(last_name) < 2:
            raise forms.ValidationError("Last name must be atleast 2 characters")
        if not last_name.replace(" ", "").isalpha():
            raise forms.ValidationError("Last name must be alpha characters")
        return last_name

    def clean_phone(self, *args, **kwags):
        phone = self.cleaned_data.get("phone").replace(" ", "")
        if not 8 < len(phone) < 14:
            raise forms.ValidationError(
                "Number must be between 9 and 13 characters, spaces are not counted"
            )
        return phone
