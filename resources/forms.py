from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailInput, TextInput, Select, DateInput, RadioSelect, CheckboxInput
from .models import AuditServiceCharter, CustomerSurvey


class AuditServiceCharterForm(ModelForm):
    class Meta:
        model = AuditServiceCharter
        fields = [
            'organization',
            'name',
            'title',
            'date_created',
            'receipt_issue',
            'complaint_log',
            'complaint_address',
            'satisfaction',
            'license_payment_processing',
            'automated_license_system',
            'response',
            'comments',
            'mode_of_response',
            'email',
        ]


class CustomerSurveyForm(ModelForm):
    class Meta:
        model = CustomerSurvey
        fields = [
            'organisation',
            'name',
            'date_created',
            'Quality',
            'integrity',
            'service_delivery',
            'problem_solving',
            'response',
            'comments',
            'email',
        ]

        widgets = {

            'organisation': TextInput(attrs={

            }),

            'name': TextInput(attrs={
                'placeholder': 'Your Full Name'
            }),

            'date_created': DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'Quality': RadioSelect(
                attrs={
                    'style': 'display:flex'
                }
            ),
            'integrity': RadioSelect(
                attrs={
                    'style': 'display:flex'
                }
            ),
            'service_delivery': RadioSelect(
                attrs={
                    'style': 'display:flex'
                }
            ),
            'problem_solving': RadioSelect(
                attrs={
                    'style': 'display:flex'
                }
            ),
            'response': RadioSelect(
                attrs={
                    'style': 'display:flex'
                }
            ),
            'comments': Textarea(),
            'email': EmailInput()
        }
