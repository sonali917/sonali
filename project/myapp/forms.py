from django import forms
from django.forms import inlineformset_factory
from .models import Company,User


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)


MaterialsFormset = inlineformset_factory(Company, User, fields=('username', 'password', 'firstname', 'lastname'),
                                         can_delete=False, extra=3)