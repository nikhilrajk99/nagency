from django import forms
from . models import Agency
class AgencyForm(forms.ModelForm):
    class Meta:
        model=Agency
        fields=['name','desc','img','date']


