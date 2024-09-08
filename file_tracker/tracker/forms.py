from django import forms
from .models import File
from django.contrib.auth.models import User

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['unique_id', 'file_name']
from django import forms
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    file = forms.FileField()
    comment = forms.CharField(widget=forms.Textarea, required=False)

class PassFileForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, label="Select User")