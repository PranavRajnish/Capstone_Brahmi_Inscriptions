from socket import fromshare
from django import forms
from .models import ImageInfo

class ImageInfoForm(forms.ModelForm):
    class Meta():
        model = ImageInfo
        fields = ('image_name', 'image')
        widgets = {
            'image_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }