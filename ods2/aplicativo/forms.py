from django import forms

class odsForm(forms.Form):
    nome = forms.CharField(max_length=50, required= True)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if len(nome) < 5:
            raise forms.ValidationError('Min 5 caracteres')
        return nome