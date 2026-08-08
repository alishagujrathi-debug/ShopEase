from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        for field in self.fields.values():

            field.widget.attrs.update({

                'class': 'form-control',

                'placeholder': field.label

            })