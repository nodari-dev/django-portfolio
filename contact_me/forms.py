from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'last_name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'text': forms.TextInput(attrs={'placeholder': 'Type here something'}),
        }