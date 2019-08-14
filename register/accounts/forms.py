from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    rodo = forms.BooleanField(required=False, help_text="I agree to accept RODO conditions")
    regulations = forms.BooleanField(required=False, help_text="I agree to accept regulations")

    class Meta:
        model = User
        fields = ('username', 'email', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
