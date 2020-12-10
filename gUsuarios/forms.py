from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['username'].widget.attrs['name'] = 'email'

        self.fields['password'].widget.attrs['class'] = 'input100'
        self.fields['password'].widget.attrs['name'] = 'pass'
       


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','email')

        labels = {
            'username' : 'Usuario',
        }
        widgets = {      
            'username' : forms.TextInput(attrs={'class':'input100'}),
            'first_name': forms.TextInput(attrs={'class':'input100'}),
            'last_name' : forms.TextInput(attrs={'class':'input100'}),
            'email' : forms.EmailInput(attrs={'class':'input100'}),
            # 'password1' : forms.PasswordInput(attrs={'class':'input100'}),
            # 'password2' : forms.PasswordInput(attrs={'class':'input100'}),
        }