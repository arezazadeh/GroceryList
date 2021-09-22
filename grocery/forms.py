from django import forms
from django.forms import ModelForm, fields

from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = ["comment"]
      
  
class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ["title", "post"]
        
class MenuForm(forms.ModelForm):
    class Meta:
        model = PersonalMenu
        fields = ["dish", "instruction"]
        
