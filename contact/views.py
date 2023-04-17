from django.shortcuts import render, redirect
from django.db.models import Count

from base.models import CallToActionPanel
from .forms import FeedbackForm, RateUsForm
from .models import RateUs
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from blog.models import Post, Category
from django.http import JsonResponse

# Create your views here.


def contact_view(request):
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    post_category = Category.objects.all()
    form = SubscriptionForm()

    cta = CallToActionPanel.objects.filter(status=1)[:1]
    form2 = FeedbackForm()
    queryset = RateUs.objects.values('rate').annotate(count=Count('rate'))


    context = {
        'form': form,
        'form2': form2,
        'cta': cta,
        'project_category': project_category,
        'publication_category': publication_category,
        'post_category': post_category,
        'rate': queryset,
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
        return redirect('contact')
    else:
        messages.error(request, 'Invalid form submission.')
    return redirect('contact')


def subscription_form_view(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
    else:
        messages.error(request, 'Invalid form submission.')
    return redirect('contact')
   