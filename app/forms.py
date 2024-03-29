from django import forms
from app.models import *

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        help_texts={'username':''}
        widgets={'password':forms.PasswordInput}

class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields=['Address','Profile_pic']
