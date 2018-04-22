from django.forms import ModelForm
from django import forms
from .models import OrderItems

class OrderForm(ModelForm):


    OPTIONS = (
        ('Waiting for Approval', 'Waiting for Approval'),
        ('Approved', 'Approved'),
        ('In Progress', 'In Progress'),
        ('Provisioned', 'Provisioned'),
        ('Not Approved', 'Not Approved')
        )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS, widget=forms.RadioSelect)

    class Meta:
        model = OrderItems
        fields = ['dept_name','app_name','function','vCPU','RAM','storage','amount','order_status']