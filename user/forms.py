from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = "Benutzername")
    password = forms.CharField(label = "Kennwort",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Benutzername")
    password = forms.CharField(max_length=20,label = "Kennwort",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Bestätige Ihr Kennwort",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError(" Kenntwort stimmt nicht überein...")

        values = {
            "username" : username,
            "password" : password
        }
        return values


