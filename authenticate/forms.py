from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .attrs import attrs

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
            if field.name == 'password':
                continue
            output.append(f'<div class="mb-3">{field.label_tag()}{field}</div>')
        return mark_safe('\n'.join(output))