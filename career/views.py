from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import JobAdvert, Tender,  PrequalifiedTender, ContractAward
from blog.models import Post, Category
from base.forms import SubscriptionForm
from.forms import SupplierRegistrationForm
from.forms import SupplierRegistrationForm
from resources.models import PubCategory
from projects.models import ProjectCategory

# Create your views here.


class CareerList(ListView):
    template_name = 'career.html'
    paginate_by: int = 8
    queryset = JobAdvert.objects.filter(status=1).order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super(CareerList, self).get_context_data(**kwargs)
        

        context['post'] = Post.objects.filter(
            status=1).order_by('-created_on')[:4]
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['post_category'] = Category.objects.all()
        context['form'] = SubscriptionForm()

        return context


class careerDetail(DetailView):
    model = JobAdvert
    template_name = 'career-info.html'

    def get_context_data(self, **kwargs):
        context = super(careerDetail, self).get_context_data(**kwargs)
        context['post'] = Post.objects.filter(
            status=1).order_by('created_on')[:4]
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['post_category'] = Category.objects.all()
        context['form'] = SubscriptionForm()

        return context


def tender_view(request):
    tender = Tender.objects.filter(status=1).all()
    post = Post.objects.filter(status=1).order_by('-created_on')[:4]
    post_category = Category.objects.all()
    publication_category = PubCategory.objects.all()
    project_category = ProjectCategory.objects.all()
    prequalified_tender = PrequalifiedTender.objects.all()
    contract_award = ContractAward.objects.all()
    
    
    prequalified_tender = PrequalifiedTender.objects.all()
    contract_award = ContractAward.objects.all()
    
    
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
    form = SubscriptionForm()

    if request.method == 'POST':
        supplier_registration = SupplierRegistrationForm(request.POST)
        if supplier_registration.is_valid():
            form.save()
    supplier_registration = SupplierRegistrationForm()

    if request.method == 'POST':
        supplier_registration = SupplierRegistrationForm(request.POST)
        if supplier_registration.is_valid():
            form.save()
    supplier_registration = SupplierRegistrationForm()
    context = {
        'tender': tender,
        'post': post,
        'form': form,
        'publication_category': publication_category,
        'project_category': project_category,
        'supplier_registration': supplier_registration,
        'prequalified_tender': prequalified_tender,
        'contract_award': contract_award,
        'supplier_registration': supplier_registration,
        'prequalified_tender': prequalified_tender,
        'contract_award': contract_award,
        'post_category': post_category
    }
    return render(request, 'tenders.html', context)
