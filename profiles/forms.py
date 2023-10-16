from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    
    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].label = False
    #     self.fields['last_name'].label = False

    #     for field_name in self.fields:
    #         field = self.fields.get('first_name')
    #         field.widget.attrs['placeholder'] = 'First Name'
    #         # field.label = 'first_name'

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']