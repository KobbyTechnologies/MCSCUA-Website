from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Faq, Publication, Terms, Privacy, PubCategory
from blog.models import Post
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from .forms import CustomerSurveyForm, AuditServiceCharterForm
from django.contrib import messages
import os

# Create your views here


def reports_view(request, pk):
    publication_category = PubCategory.objects.all()
    publication_category_in = PubCategory.objects.get(id=pk)
    publication = Publication.objects.filter(status=1, category=pk).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    project_category = ProjectCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'subscription was submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    form = SubscriptionForm()
    context = {
        'pub': publication,
        'post': post,
        'form': form,
        'publication_category': publication_category,
        'publication_category_in': publication_category_in,
        'project_category': project_category,
    }
    return render(request, 'reports.html', context)



def faq_view(request):
    faq = Faq.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'subscription was submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    form = SubscriptionForm()
    context = {
        
        'faq': faq,
        'post': post,
        'form': form,
        'project_category': project_category,
    }
    return render(request, 'faq.html', context)


def terms(request):
    terms = Terms.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'subscription was submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    form = SubscriptionForm()
    context = {
        'terms': terms,
        'post': post,
        'form': form,
        'project_category': project_category,
    }
    return render(request, 'terms.html', context)


def privacy(request):
    privacy = Privacy.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    form = SubscriptionForm()
    context = {
        'privacy': privacy,
        'post': post,
        'form': form,
        'project_category': project_category,
    }
    return render(request, 'privacy.html', context)

def auditServiceView(request):
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')

    AuditCharterForm = AuditServiceCharterForm()
    
    if request.method == 'POST':
        AuditCharterForm = AuditServiceCharterForm(request.POST)
        if AuditCharterForm.is_valid():
            AuditCharterForm.save()
            messages.success(request, 'Submitted successfully')
        else:
            messages.success(request, 'Invalid form submission.')
    context = {
        'AuditCharterForm': AuditCharterForm,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'audit_service.html', context)

def customerSurvey(request):
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
    form = SubscriptionForm()

    if request.method == 'POST':
        customer_survey = CustomerSurveyForm(request.POST)
        if customer_survey.is_valid():
            customer_survey.save()
            messages.success(request, 'submitted successfully.')
            return redirect('customerSurvey')
        else:
            messages.error(request, 'Invalid form submission.')
            print(form.errors)
    
    customer_survey = CustomerSurveyForm()

    context = {
        'form': form,
        'customer_survey': customer_survey,
        'project_category': project_category,
        'publication_category': publication_category,
    }

    return render(request, 'customer_request.html', context)

