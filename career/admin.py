from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import JobAdvert, Tender, Service, SupplierRegistrationDetails, ContractAward, PrequalifiedTender, Service, SupplierRegistrationDetails, ContractAward, PrequalifiedTender


class JobAdvertAdmin(SummernoteModelAdmin):
    summernote_fields = ['qualification', 'resposibilities', 'how_to_apply']

    fields = (
        'title',
        'slug',
        'job_ID',
        'job_description',
        'qualification',
        'resposibilities',
        'how_to_apply',
        'advert_file',
        'deadline',
        'job_status',
        'job_type',
        'status'
    )

    list_display = ('title', 'job_ID', 'short_description',
                    'job_type', 'deadline', 'status')
    list_display_links = ('title', 'job_ID')
    list_filter = ('pub_date',)
    search_fields = ('title', 'job_ID')
    prepopulated_fields = {'slug': ('title', 'job_ID')}


class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'ref_number', 'short_description', 'status')
    list_filter = ('pub_date',)


# Register your models here.
admin.site.register(JobAdvert, JobAdvertAdmin)
admin.site.register(Tender, TenderAdmin)
admin.site.register(ContractAward)
admin.site.register(Service)
admin.site.register(SupplierRegistrationDetails)
admin.site.register(PrequalifiedTender)

