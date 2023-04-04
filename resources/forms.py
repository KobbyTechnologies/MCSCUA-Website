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
            'organization',
            'name',
            'title',
            'date_created',
            'Quality',
            'integrity',
            'service_delivery',
            'problem_solving',
            'response',
            'comments',
            'mode_of_response',
            'mode_of_response_type',
            'email',
        ]
