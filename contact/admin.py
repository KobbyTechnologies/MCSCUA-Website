from django.contrib import admin
from .models import Feedback, RateUs
from import_export.admin import ExportActionMixin


class FeedbackAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display= ['name', 'subject', 'type', 'pub_date']
    list_filter = ['pub_date',]
    search_fields = ['name', 'subject']
    readonly_fields = ['type','name','email', 'subject', 'message', 'pub_date']

    def has_add_permission(self, request, obj=None):
        return False
    
class RateusAdmin(ExportActionMixin,admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(RateUs, RateusAdmin)