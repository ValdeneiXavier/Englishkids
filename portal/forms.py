from django import forms
from portal.models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ('nome','telefone','data_nascimento', 'email')

        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'telefone' : forms.TextInput(attrs={'class':'form-control','autofocus':''}),
            'data_nascimento': forms.DateInput(attrs={'class':'form-control'},format='%d/%m/%Y'),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
