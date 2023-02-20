from django.shortcuts import render, redirect
from base.models import CallToActionPanel
from .forms import FeedbackForm, RateUsForm
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

    form = SubscriptionForm()

    cta = CallToActionPanel.objects.filter(status=1)[:1]
    form2 = FeedbackForm()
    context = {
        'form': form,
        'form2': form2,
        'cta': cta,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'contact.html', context)


def feedback_form(request):

    feedback = FeedbackForm()
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()
            messages.success(
                request, 'The Request was submitted successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Invalid form submission.')

    return redirect('index')


def RateUs_view(request):
    rateUsForm = RateUsForm()
    if request.method == 'POST':
        rateUsForm = RateUsForm(request.POST)
        rateUsForm.save()
        messages.success(request, 'Thank you for rating our services.')
        return redirect('index')
    else:
        messages.error(request, 'Invalid form submission.')
    return redirect('index')


def subscription_form_view(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'submitted successfully.')
    else:
        messages.error(request, 'Invalid form submission.')
    return redirect('index')
   