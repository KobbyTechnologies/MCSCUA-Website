from django.shortcuts import render
from  .models import Service
from base.models import CallToActionPanel

# Create your views here.

def service_view(request):
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    service = Service.objects.all()
    context = {
        'cta': cta,
        'services':service,
    }
    return render(request, 'service.html', context)
