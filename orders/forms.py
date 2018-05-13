from django.forms import ModelForm
from django import forms
from .models import OrderItems1
from .models import TotalCosts

class OrderForm(ModelForm):


    OPTIONS = (
        ('Waiting for Approval', 'Waiting for Approval'),
        ('Approved', 'Approved'),
        ('In Progress', 'In Progress'),
        ('Provisioned', 'Provisioned'),
        ('Not Approved', 'Not Approved')
        )
    OPTIONS_DR = (
        ('',''),
        ('Yes','Yes'),
        ('No','No')
    )

    OPTIONS_OS = (
        ('',''),
        ('Windows','Windows'),
        ('RHEL','RHEL'),
        ('Suse','Suse'),
        ('Others','Others')
    )

    OPTIONS_DB = (
        ('',''),
        ('Oracle','Oracle'),
        ('SQL','SQL')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS, widget=forms.RadioSelect)
    dr = forms.TypedChoiceField(choices=OPTIONS_DR)
    os = forms.TypedChoiceField(choices=OPTIONS_OS)
    db = forms.TypedChoiceField(choices=OPTIONS_DB)


    class Meta:
        model = OrderItems1
        fields = ['dept_name','app_name','function','vCPU','RAM','storage','amount','order_status','dr','os','db']


class TotalForm(ModelForm):
    class Meta:
        model = TotalCosts
        fields = ['totalDC','totalServer','totalNetwork' ,'LMF','totalvCPU','totalRAM','totalStorage','microsoft','redhat','suse','otherOS','oracle','sql','totalStorageCost']