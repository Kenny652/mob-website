from django import forms 

from .models import Annonce

class AnnoncesModelForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = [
            'title',
            'description',
            'content',
        ]
        widgetds = {
            'title'       : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class': 'form-control'}),
            'content'     : forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
        }

        

