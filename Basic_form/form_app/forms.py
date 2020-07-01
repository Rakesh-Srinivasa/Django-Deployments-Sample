from django import forms
from django.forms import ModelForm
#from django import validators
from form_app.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
