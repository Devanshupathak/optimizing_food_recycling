from django import forms
from .models import FoodItem
from .models import Donor

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'expiration_date', 'quantity', 'donor']  

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'email', 'phone', 'address']