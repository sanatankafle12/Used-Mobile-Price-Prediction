from django import forms
from .models import Listing

class valuate_listing(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['brand','model','description','battery','back_camera','front_camera','ram','storage','price','size','res','image','condition']
        
