from django.shortcuts import render
from .forms import PostSearchForm
from resources.models import Publication

from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank, TrigramSimilarity, TrigramDistance

# Create your views here.
def post_search(request):
    search_form = PostSearchForm

    results = []

    if 'q' in request.GET:
        search_form = PostSearchForm(request.GET)
        if search_form.is_valid():
            q = search_form.cleaned_data['q']
        
            # results = Publication.objects.filter(name__search = q)
            # results = Publication.objects.annotate(search = SearchVector('name', 'category'),).filter(search=q)

            vector = SearchVector('name', 'category')
            query = SearchQuery(q)

            # results = Publication.objects.annotate(rank = SearchRank(vector, query),).order_by('-rank')
            
            
            # results = Publication.objects.annotate(similarity = TrigramSimilarity('name', q),).filter(similarity__gte = 0.1).order_by('-similarity')
            results = Publication.objects.annotate(distance = TrigramDistance('name', q),).filter(distance__lte = 0.8).order_by('distance')

    ctx = {
        'search_form': search_form,
        'results': results,
        # 'q': q,
    }
    return render(request, 'base-search.html', ctx)