from django import forms
from hcaptcha.fields import hCaptchaField


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    hcaptcha = hCaptchaField()
