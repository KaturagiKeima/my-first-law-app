from django import forms
from .models import Contact
 
class Answer1(forms.Form):
    answer = forms.CharField(max_length=1000, label="答え")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "title", "body"]
        