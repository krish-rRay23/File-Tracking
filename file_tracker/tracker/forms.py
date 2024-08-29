from django import forms
from .models import File
from django.contrib.auth.models import User

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['unique_id', 'file_name']

class PassFileForm(forms.Form):
    passed_to = forms.ModelChoiceField(queryset=User.objects.all())
