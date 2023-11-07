from django import forms

from website.models import Contact, Newsletter
from captcha.fields import ReCaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    

    
class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Contact
        fields = '__all__'


        
class NewsletterForm(forms.ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Newsletter
        fields = '__all__'
        
