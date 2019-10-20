from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, f'{str(i)} шт.') for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, label='Колличество', coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)