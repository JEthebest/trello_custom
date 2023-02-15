from django import forms

from .models import OrderCard


class OrderCardForm(forms.ModelForm):
    
    class Meta:
            model = OrderCard
            fields = "__all__"