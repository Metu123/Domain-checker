from django import forms


class DomainCheckForm(forms.Form):
    domain = forms.CharField(
        label='Domain or URL',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'input-field',
            'placeholder': 'Enter domain (e.g., google.com or https://example.com)',
            'autocomplete': 'off'
        })
    )
