from .models import datas
from django import forms

class dataForm(forms.ModelForm):
    class Meta:
        model = datas
        fields = ['SL_NO','ITEM_NAME','DESCRIPTION']

         