from django.shortcuts import render
from .models import Project, ProjectCategory
from base.models import CallToActionPanel, Subscription
from base.forms import SubscriptionForm
from resources.models import PubCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def projects_view(request, pk):
    project_list = Project.objects.filter(status=1, category=pk).all()
    project_category = ProjectCategory.objects.all()
    project_category_in = ProjectCategory.objects.get(id=pk)
    publication_category = PubCategory.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(project_list, 8) # Show 8 projects per page.

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
       projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    

    context = {
        'cta': cta,
        'projects': projects,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
        'project_category_in': project_category_in,
        
    }
    return render(request, 'projects.html', context)


def project_detail_view(request, slug):
    projects = Project.objects.get(slug=slug)
    project_category = ProjectCategory.objects.all()
    
    publication_category = PubCategory.objects.all()
    cta = CallToActionPanel.objects.filter(status=1)[:1]
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()
    context = {
        'cta': cta,
        'projects': projects,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
        
    }
    return render(request, 'project-detail.html', context)    

