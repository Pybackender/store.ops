from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.NumberInput(attrs={
            'min': 1,  # Minimum value
            'max': 20,  # Maximum value
            'step': 1,  # Step size
            'class': 'form-control'  # Optional: Add a class for styling
        })
    )
    override = forms.BooleanField(required=False,
                                   initial=False,
                                   widget=forms.HiddenInput)
