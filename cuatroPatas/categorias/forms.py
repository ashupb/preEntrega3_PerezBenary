from django import forms 

class CollaresForm(forms.Form):
    tipo = forms.CharField(max_length=50, required=True) 
    tamanio = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True) 

class AlimentacionForm(forms.Form):
    tipo = forms.CharField(max_length=50, required=True) 
    tamanio = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)

class ConfortForm(forms.Form):
    tipo = forms.CharField(max_length=50, required=True) 
    precio = forms.IntegerField(required=True)

