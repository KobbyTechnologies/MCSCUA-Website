from django.shortcuts import render, redirect
from base.models import CallToActionPanel
from .forms import FeedbackForm
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def contact_view(request):
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()

    #  subscription form feedback
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'submitted successfully.')
    else:
        messages.error(request, 'Invalid form submission.')
            
    form = SubscriptionForm()

    # contact us form feedback
    if request.method == 'POST':
        form2 = FeedbackForm(request.POST)
        if form2.is_valid():
            # subject = form2.cleaned_data['subject']
            # body = {
            #     'Name': form2.cleaned_data['name'],
            #     'Email': form2.cleaned_data['email'],
            #     'Type': form2.cleaned_data['type'],
            #     'Message': form2.cleaned_data['message'],
            # }
            # message = "\n".join(body)
            # try:
            #     send_mail(subject, message, 'admin@example.com',
            #               ['admin@example.com'])
            # except:
            #     return HttpResponse('Invalid header found.')
            # form2.save()
            messages.success(request, 'submitted successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Invalid form submission.')
           

    form2 = FeedbackForm()

    cta = CallToActionPanel.objects.filter(status=1)[:1]

    context = {
        'form': form,
        'form2': form2,
        'cta': cta,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'contact.html', context)


def feedback_view(request):
    return render(request, 'feedback.html')
