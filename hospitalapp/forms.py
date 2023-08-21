from django import forms 
from .models import doctor


class AddForm(forms.ModelForm):
    class Meta:
        model =  doctor
        
        fields = ('name','age','department','email','username','password')
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }