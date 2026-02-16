from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'item_order', 'first_name', 'last_name', 'email_address',
            'phone_number', 'payment_method', 'delivery_address', 'comment'
        ]
        widgets = {
            'item_order': forms.TextInput(attrs={'readonly': 'readonly'}),
            'delivery_address': forms.Textarea(attrs={'rows': 2}),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Optional'}),
        }
        labels = {
            'item_order': 'Item Order',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'payment_method': 'Payment Method',
            'delivery_address': 'Delivery Address',
            'comment': 'Comment',
        }

    def __init__(self, *args, user=None, item=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields['first_name'].initial = user.first_name or ''
            self.fields['last_name'].initial = user.last_name or ''
            self.fields['email_address'].initial = user.email or ''
            self.fields['phone_number'].initial = getattr(user, 'phone', '') or ''
            self.fields['payment_method'].initial = getattr(user, 'payment', '') or ''
            self.fields['delivery_address'].initial = getattr(user, 'address', '') or ''

        if item:
            self.fields['item_order'].initial = item.name_en
            self.instance.item = item

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'item_order':
                field.widget.attrs['readonly'] = 'readonly'
            elif field_name == 'payment_method':
                field.widget.attrs.update({'placeholder': 'Method and bank name'})
            elif field_name == 'delivery_address':
                field.widget.attrs.update({'rows': 2, 'placeholder': 'Country and delivery address'})
            elif field_name == 'comment':
                field.widget.attrs.update({'rows': 4, 'placeholder': 'Optional'})
            else:
                field.widget.attrs['placeholder'] = field.label
