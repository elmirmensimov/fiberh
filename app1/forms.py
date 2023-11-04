from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Link"}),
            'email': forms.EmailInput(attrs={'placeholder': "Email"}),
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': "Məhsulun ölçüsü, rəngi və.s haqda məlumat"}),
        }


