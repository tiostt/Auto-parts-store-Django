from django import forms


class CreateOrderForm(forms.Form):

    phone_number = forms.CharField()
    delivery_address = forms.CharField(required=False)