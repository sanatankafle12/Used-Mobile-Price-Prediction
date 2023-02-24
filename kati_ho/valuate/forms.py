from django import forms
from .models import Listing

class valuate_listing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['brand','model','description','battery','back_camera','front_camera','ram','storage','price','size','res','condition']
"""         widgets = {
            'model':forms.TextInput(attrs={'class':'form-control'}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'battery':forms.TextInput(attrs={'class':'form-control'}),
            'front_camera':forms.TextInput(attrs={'class':'form-control'}),
            'back_camera':forms.TextInput(attrs={'class':'form-control'}),
            'ram':forms.TextInput(attrs={'class':'form-control'}),
            'storage':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'size':forms.TextInput(attrs={'class':'form-control'}),
            'condition':forms.TextInput(attrs={'class':'form-control'}),
        } """
