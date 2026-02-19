from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'name_jp', 'first_name', 'last_name', 'email',
            'phone', 'payment', 'address', 'comment'
        ]
        widgets = {
            'name_jp': forms.TextInput(attrs={'readonly': 'readonly'}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'name_jp': 'Name (JP)',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'payment': 'Payment Method',
            'address': 'Delivery Address',
            'comment': 'Comment',
        }

    def __init__(self, *args, user=None, collection=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['first_name'].initial = user.first_name or ''
            self.fields['last_name'].initial = user.last_name or ''
            self.fields['email'].initial = user.email or ''
            self.fields['phone'].initial = getattr(user, 'phone', '') or ''
            self.fields['payment'].initial = getattr(user, 'payment', '') or ''
            self.fields['address'].initial = getattr(user, 'address', '') or ''

        if collection:
            self.fields['name_jp'].initial = collection.name_jp

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'name_jp':
                field.widget.attrs['readonly'] = 'readonly'
            elif field_name == 'payment':
                field.widget.attrs.update({'placeholder': 'Method and bank name'})
            elif field_name == 'address':
                field.widget.attrs.update({'rows': 2, 'placeholder': 'Country and delivery address'})
            elif field_name == 'comment':
                field.widget.attrs.update({'rows': 4, 'placeholder': 'Optional'})
            else:
                field.widget.attrs['placeholder'] = field.label
