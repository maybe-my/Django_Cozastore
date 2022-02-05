from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                label='',
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int,
                                widget=forms.NumberInput(attrs={'class': 'mtext-104 cl3 txt-center num-product',
                                                                'value': 1,
                                                                'name': 'num-product',
                                                                'type': 'number'}))
    # update = forms.BooleanField(required=False,
    #                             initial=False,
    #                             widget=forms.HiddenInput)
