from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo, CustomUser
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "deadline"]


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem.")

        # Valida a força da senha
        self.validate_password_strength(password1)

        return password2

    def validate_password_strength(self, password):
        min_length = 5
        errors = []

        if len(password) < min_length:
            errors.append(f"A senha deve ter pelo menos {min_length} caracteres.")

        if not any(char.isdigit() for char in password):
            errors.append("A senha deve conter pelo menos um número.")

        if not any(char.isalpha() for char in password):
            errors.append("A senha deve conter pelo menos uma letra.")

        if not any(char.isupper() for char in password):
            errors.append("A senha deve conter pelo menos uma letra maiúscula.")

        if not any(char.islower() for char in password):
            errors.append("A senha deve conter pelo menos uma letra minúscula.")

        special_characters = "!@#$%^&*()_+-=,./<>?;:[]{}|~"
        if not any(char in special_characters for char in password):
            errors.append("A senha deve conter pelo menos um caractere especial.")

        if errors:
            raise ValidationError(errors)


class CustomAuthenticationForm(AuthenticationForm):
    pass
