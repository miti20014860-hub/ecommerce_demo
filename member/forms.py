from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm as BasePasswordChangeForm
from django.core.exceptions import ValidationError
from .models import CustomUser


# ==================== 登入表單 ====================
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label="Password"
    )

    error_messages = {
        'invalid_login': "Incorrect account or password",
    }


# ==================== 註冊表單 ====================
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        label='Username'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
        label='Email Address'
    )
    password1 = forms.CharField(
        label='Create a Password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control', 'placeholder': 'Create a Password',
                'title': 'Password must at least 8 characters and cannot be entirely numeric'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
        (attrs={'class': 'form-control', 'placeholder': 'Confirm Password',
                'title': 'Password must at least 8 characters and cannot be entirely numeric'})
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# ==================== 個人資料編輯 ====================
class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    phone = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    current_password = forms.CharField(
        required=True,
        label="Current Password",
        help_text="Confirm Profile Changes",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Profile Changes.'
        }),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['phone'].initial = self.instance.phone
            self.fields['address'].initial = self.instance.address

    def clean_current_password(self):
        password = self.cleaned_data.get('current_password')
        if not self.instance.check_password(password):
            raise ValidationError("Incorrect Password.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


# ==================== 密碼變更 ====================
class PasswordChangeForm(BasePasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['old_password', 'new_password1', 'new_password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter password to confirm password changes.',
                'title': 'Password must at least 8 characters and cannot be entirely numeric',
            })

        self.fields['old_password'].label = "Current Password"
        self.fields['new_password1'].label = "Enter New Password"
        self.fields['new_password2'].label = "Confirm New Password"
