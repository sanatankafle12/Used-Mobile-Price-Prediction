from django import forms
from .models import Listing

class valuate_listing(forms.ModelForm):
    class Meta:
        CONDITION_CHOICES = [i for i in range(1, 11)]
        model = Listing
        fields = ['brand','model','description','battery','back_camera','front_camera','ram','storage','price','size','res','image','condition']
        
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'battery': forms.NumberInput(attrs={'class': 'form-control'}),
            'back_camera': forms.NumberInput(attrs={'class': 'form-control'}),
            'front_camera': forms.NumberInput(attrs={'class': 'form-control'}),
            'ram': forms.NumberInput(attrs={'class': 'form-control'}),
            'storage': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'res': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'storage': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        