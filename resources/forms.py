from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea, EmailInput, TextInput, Select, DateInput, RadioSelect, CheckboxInput
from .models import AuditServiceCharter, CustomerSurvey


class AuditServiceCharterForm(ModelForm):
    class Meta:
        model = AuditServiceCharter
        fields = [

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

            'name':TextInput(attrs={
                'placeholder': 'Your Full Name'
            }),

            'date_created':DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'Quality':RadioSelect(
                attrs={
                    'style':'display:flex'
                }
            ),
            'integrity':RadioSelect(),
            'service_delivery':RadioSelect(),
            'problem_solving':RadioSelect(),
            'response':RadioSelect(),
            'comments':Textarea(),
        }
