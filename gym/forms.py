from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MembershipApplication

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class MembershipApplyForm(forms.ModelForm):
    class Meta:
        model = MembershipApplication
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }
