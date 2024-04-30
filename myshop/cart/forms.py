from django import forms

# Define choices for product quantity to allow the users to select
# a quantity between 1 and 20
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    """Form for adding a product to the shopping cart.
    """
    # Field for selecting quantity
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int) # Ensure the input is converted to an integer
    
    # Field for overriding quantity (hidden by default)
    override = forms.BooleanField(required=False, # Not required, as it's hidden by default
                                  initial=False, # Default value is False
                                  widget=forms.HiddenInput) # Hide the field in the form