from django.views.generic import ListView, DetailView
from django.shortcuts import render,  get_object_or_404
from django.db.models import Q
from .models import Post, Featured, Category
from projects.models import Project, ProjectCategory
from resources.models import PubCategory
from base.forms import SubscriptionForm


# Create your views here.

class PostList(ListView):
    template_name = 'post.html'
    paginate_by: int = 9

    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(status=1,category=self.kwargs['pk']).order_by('-created_on')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['post_category'] = Category.objects.all()
        context['form'] = SubscriptionForm()
        
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['post_category'] = Category.objects.all()
        context['form'] = SubscriptionForm()

        return context


class FeaturedList(ListView):
    template_name = 'featuredArticles.html'
    paginate_by: int = 9
    context_object_name = 'featured_list'
    queryset = Featured.objects.filter(status=1).order_by('-created_on')

    def get_object_data(self, **kwargs):
        context = super(FeaturedList, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['post_category'] = Category.objects.all()
        context['form'] = SubscriptionForm()

        return context
