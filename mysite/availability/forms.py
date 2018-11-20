from django import froms
from django.contrib.auth.forms import UsernameField

class ContactForm(forms.Form):
    """Login Form"""
    FirstName = UsernameField(
        label='First Name',
        max_length=30,
    )

    LastName
