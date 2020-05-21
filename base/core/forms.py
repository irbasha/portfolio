from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-field',
        'type': 'text',
        'name': 'contactName',
        'id': 'contactName',
        'placeholder': 'Name',
    }))
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-field',
        'type': 'email',
        'name': 'contactEmail',
        'id': 'contactEmail',
        'placeholder': 'Email',
    }))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-field',
        'type': 'text',
        'name': 'contactSubject',
        'id': 'contactSubject',
        'placeholder': 'Subject',
    }))
    message = forms.CharField(max_length=100, required=True, widget=forms.Textarea(attrs={
        'class': 'form-field',
        'name': 'contactMessage',
        'id': 'contactMessage',
        'placeholder': 'Message',
        'rows': 10,
        'columns': 50,
    }))
