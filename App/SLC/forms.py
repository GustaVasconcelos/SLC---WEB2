from django import forms
from .models import Lista
from .models import Itens

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['titulo']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = ['texto']