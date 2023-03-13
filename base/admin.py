from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin
from base.models import Carousel, Patner, Subscription, CallToActionPanel, Empowerment
from import_export.admin import ExportActionMixin

class CarouselAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'photo',
        'title',
        'caption',
        'status',
    )

    list_display = [
        'photo',
        'title',
        'short_description',
        'status',
        'created_on',
        
    ]
    list_display_links = ['title']
    list_filter = ['status', 'created_on']
    search_fields = ['title', 'caption']
    readonly_fields = ['photo', 'created_on', ]


class PatnerAdmin(admin.ModelAdmin):

    fields = ('image', 'name', 'caption', 'url', 'status')

    list_display = [
        'org_photo',
        'name',
        'short_description',
        'status',
    ]

    list_display_links = ['name']
    list_filter = ['status', ]
    search_fields = ['name', 'caption']


class CallToActionPanelAdmin(admin.ModelAdmin):
    fields = ('image', 'title', 'url', 'description', 'status')

    list_display = [
        'photo',
        'title',
        'short_description',
        'status',
    ]
    list_display_links = ['title']
    list_filter = ["status",]
    search_fields = ['title', 'description']


class EmpowermentAdmin(admin.ModelAdmin):
    list_display = ['bg_photo','title', 'short_desctiption', 'status']
    list_filter = ['pub_date']


class SubscriptionAdmin(ExportActionMixin,admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

# Register your models here.
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Patner, PatnerAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(CallToActionPanel, CallToActionPanelAdmin)
admin.site.register(Empowerment)


# Dashboad Customization
admin.site.site_header = "MCSCUA Dashboard"
admin.site.unregister(Group)
