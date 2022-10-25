from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Faq, Publication, Terms, Privacy, PubCategory
from blog.models import Post
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
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
    form = SubscriptionForm()
    context = {
        'privacy': privacy,
        'post': post,
        'form': form,
        'project_category': project_category,
    }
    return render(request, 'privacy.html', context)
