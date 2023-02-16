from django.views.generic import ListView, DetailView
from django.shortcuts import render,  get_object_or_404
from django.db.models import Q
from .models import Post, Featured
from projects.models import Project, ProjectCategory
from resources.models import PubCategory
from base.forms import SubscriptionForm


# Create your views here.

class PostList(ListView):
    template_name = 'post.html'
    paginate_by: int = 9
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['form'] = SubscriptionForm()

        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
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
        context['form'] = SubscriptionForm()

        return context



def search(request):

    keywords = ''

    if request.method == 'POST':  # form was submitted

        # <input type="text" name="keywords">
        keywords = request.POST.get("keywords", "")
        all_queries = None
        search_fields = ('title', 'content', 'resume')  # change accordingly
        # keywords are splitted into words (eg: john science library)
        for keyword in keywords.split(' '):
            keyword_query = None
            for field in search_fields:
                each_query = Q(**{field + '__icontains': keyword})
                if not keyword_query:
                    keyword_query = each_query
                else:
                    keyword_query = keyword_query | each_query
                    if not all_queries:
                        all_queries = keyword_query
                    else:
                        all_queries = all_queries & keyword_query

        articles = Post.objects.filter(all_queries).distinct()
        context = {'articles': articles}
        return render(request, 'search.html', context)

    else:  # no data submitted

        context = {}
        return render(request, 'index.html', context)
