from django.contrib import admin
from resources import models
from resources.models import Faq, Publication, Privacy, Terms, PubCategory, CustomerSurvey, AuditServiceCharter
from django_summernote.admin import SummernoteModelAdmin


class FaqAdmin(SummernoteModelAdmin):
    list_display = ('question', 'short_description', 'status')
    list_filter = ['date_created', ]
    search_fields = ['question', 'answer']


class PrivacyAdmin(SummernoteModelAdmin):
    list_display = ['title', 'modified', 'status']


class TermsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'modified', 'status']


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'status']


class CustomerSurveyAdmin(admin.ModelAdmin):
    list_display = ['organization', 'name', 'title', 'date_created',]
    list_filter = ['date_created',]
    search_fields = ['organization', 'name']
    readonly_fields = [
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
        'other',
        'email',
    ]

    def has_add_permission(self, request, obj=None):
        return False


class AuditServiceCharterAdmin(admin.ModelAdmin):
    list_display = ['organization', 'name', 'title', 'date_created',]
    list_filter = ['date_created',]
    search_fields = ['organization', 'name']
    readonly_fields = [
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
        'comments',
        'mode_of_response',
        'response',
        'email'
    ]


# Register your models here.
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Privacy, PrivacyAdmin)
admin.site.register(PubCategory)
admin.site.register(CustomerSurvey, CustomerSurveyAdmin)
admin.site.register(AuditServiceCharter, AuditServiceCharterAdmin)
