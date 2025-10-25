from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Profile
from django import forms


class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=200, required=False)
    payment = forms.CharField(max_length=20, required=False)

    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        }),
        required=True,
        help_text="Enter password to confirm profile changes."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        profile = getattr(user, 'profile', None)

        current_phone = profile.phone if profile else ''
        self.fields['phone'].widget.attrs['placeholder'] = current_phone
        self.fields['phone'].initial = profile.phone

        current_address = profile.address if profile else ''
        self.fields['address'].widget.attrs['placeholder'] = current_address
        self.fields['address'].initial = profile.address

        current_payment = profile.payment if profile else ''
        self.fields['payment'].widget.attrs['placeholder'] = current_payment
        self.fields['payment'].initial = profile.payment

    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        if not self.user.check_password(password):
            raise ValidationError("Incorrect Password.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            profile, _ = Profile.objects.get_or_create(user=user)
            profile.phone = self.cleaned_data['phone']
            profile.address = self.cleaned_data['address']
            profile.payment = self.cleaned_data['payment']
            profile.save()

        return user
