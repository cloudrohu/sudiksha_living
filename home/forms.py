from django import forms
from .models import ContactEnquiry
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactEnquiryForm(forms.ModelForm):

    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox
    )

    class Meta:
        model = ContactEnquiry
        fields = ["type", "name", "email", "phone", "message"]