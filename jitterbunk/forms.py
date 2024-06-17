from django import forms
from .models import Bunk, User

class BunkForm(forms.ModelForm):
    from_user = forms.ModelChoiceField(queryset=User.objects.all(), label='From User')
    to_user = forms.ModelChoiceField(queryset=User.objects.all(), label='To User')
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Time')
    
    class Meta:
        model = Bunk
        fields = ['from_user', 'to_user', 'time']
