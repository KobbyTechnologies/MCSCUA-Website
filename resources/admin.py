from django.contrib import admin
from resources import models
from resources.models import Faq, Publication, Privacy,Terms, PubCategory, CustomerSurvey, AuditServiceCharter
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
    list_display= ['name', 'category', 'status']

# Register your models here.
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Privacy, PrivacyAdmin)
admin.site.register(PubCategory)
admin.site.register(CustomerSurvey)
admin.site.register(AuditServiceCharter)
