from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )    
    )


    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )

    email_cadastro = forms.CharField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@gmail.com"
            }
        )
    )

    senha_cadastro = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Digite sua senha"
            }
        )
    )

    confirmar_senha_cadastro = forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Confirme sua senha"
            }
        )
    )
    
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo Nome de Usuário.")
            else:
                return nome
