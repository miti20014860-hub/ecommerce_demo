from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    payment_method = forms.ChoiceField(
        choices=Order.PAYMENT_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'btn-check'}),
        initial='wire_transfer',
        label="Payment Method"
    )

    class Meta:
        model = Order
        fields = [
            'payment_method', 'item_order', 'first_name', 'last_name', 'email_address',
            'phone_number', 'country', 'delivery_address', 'comment'
        ]
        widgets = {
            'item_order': forms.TextInput(attrs={'readonly': 'readonly'}),
            'delivery_address': forms.Textarea(attrs={'rows': 2}),
            'comment': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Optional'}),
        }
        labels = {
            'payment_method': 'Payment Method',
            'item_order': 'Item Order',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'delivery_address': 'Delivery Address',
            'comment': 'Comment',
        }

    def __init__(self, *args, user=None, item=None, **kwargs):
        super().__init__(*args, **kwargs)

        # 自動填入登入者資料
        if user and user.is_authenticated:
            self.fields['first_name'].initial = user.first_name or ''
            self.fields['last_name'].initial = user.last_name or ''
            self.fields['email_address'].initial = user.email or ''
            self.fields['phone_number'].initial = getattr(user, 'phone', '') or ''
            self.fields['country'].initial = getattr(user, 'country', '') or ''
            self.fields['delivery_address'].initial = getattr(user, 'address', '') or ''

        # 項目名稱
        if item:
            self.fields['item_order'].initial = item.name_en

        # 自動加 Bootstrap class
        for field_name, field in self.fields.items():
            if field_name != 'payment_method':
                field.widget.attrs['class'] = 'form-control'
                if field_name == 'comment':
                    field.widget.attrs.update({'rows': 5, 'placeholder': 'Optional'})
                elif field_name == 'item_order':
                    field.widget.attrs['readonly'] = 'readonly'
                else:
                    field.widget.attrs['placeholder'] = field.label
