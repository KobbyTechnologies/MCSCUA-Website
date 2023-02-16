from pyexpat import model
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailInput, TextInput, Select, FileInput, SelectMultiple
from .models import SupplierRegistrationDetails


class SupplierRegistrationForm(ModelForm):

    class Meta:
        model = SupplierRegistrationDetails
        fields = [
            'ownership',
            'company_name',
            'KRA_pin',
            'company_email',
            'company_phone',
            'country',
            'physical_address',
            'city',
            'postal_address',
            'postal_code',
            'services',
            'full_name',
            'mobile_number',
            'email',
            'company_certificate_reg',
            'KRA_pin_certificate',
            'KRA_compliance_certificate',
            'company_memorandum_directors_page',
        ]

        widgets = {
            'ownership': Select(attrs={
                'class':"select",
            }),
            'company_name': TextInput(attrs={
                'class':"select"
            }),
            'company_name': TextInput(attrs={

            }),
            'KRA_pin': TextInput(attrs={

            }),
            'company_email': TextInput(attrs={

            }),
            'country': TextInput(attrs={

            }),
            'physical_address': TextInput(attrs={

            }),
            'city': TextInput(attrs={

            }),
            'postal_address': TextInput(attrs={

            }),
            'postal_code': TextInput(attrs={

            }),
            'full_name': TextInput(attrs={

            }),
            'services': SelectMultiple(attrs={
                'class':"select",
            }),
            'mobile_number': TextInput(attrs={

            }),
            'email': EmailInput(attrs={

            }),
            'company_certificate_reg': FileInput(attrs={

            }),
            'KRA_pin_certificate': FileInput(attrs={

            }),
            'KRA_compliance_certificate': FileInput(attrs={

            }),
            'company_memorandum_directors_page': FileInput(attrs={

            }),

        }

        
