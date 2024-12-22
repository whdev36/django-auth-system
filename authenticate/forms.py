from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        attrs = {
            'placeholder': {
                'email': 'Enter your email',
                'first_name': 'Enter your first name',
                'last_name': 'Enter your last name',
                'username': 'Create username',
                'password1': 'Create password',
                'password2': 'Confirm password',
            },
            'label': {
                'email': 'Email',
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'username': 'Username',
                'password1': 'Password',
                'password2': 'Confirm Password',
            },
            'help_text': {
                'email': 'Please enter a valid email address.',
                'first_name': 'Your first name as it appears on official documents.',
                'last_name': 'Your last name as it appears on official documents.',
                'username': 'Choose a unique username for your account.',
                'password1': 'Your password must be at least 8 characters long.',
                'password2': 'Enter the same password as above for verification.',
            },
            'error_messages': {
                'email': {
                    'required': 'Email is required.',
                    'invalid': 'Enter a valid email address.',
                },
                'username': {
                    'required': 'Username is required.',
                    'unique': 'This username is already taken.',
                },
                'password1': {
                    'required': 'Password is required.',
                    'too_short': 'Password must be at least 8 characters.',
                },
                'password2': {
                    'required': 'Please confirm your password.',
                    'mismatch': 'Passwords do not match.',
                },
            }
        }

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = attrs['placeholder'].get(field, '')
            self.fields[field].label = attrs['label'].get(field, field.capitalize())
            self.fields[field].label_suffix = ''
            self.fields[field].help_text = attrs['help_text'].get(field, '')
            self.fields[field].error_messages = attrs['error_messages'].get(field, {})

    def as_div(self):
        output = []
        for field in self:
            output.append(f'<div class="mb-3">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))

