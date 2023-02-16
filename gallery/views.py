from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import PhotoGallery, VideoGallery
from base.forms import SubscriptionForm
from projects.models import Project, ProjectCategory
from resources.models import PubCategory
from django.contrib import messages

# Create your views here.

def gallery_view(request):
    photo = PhotoGallery.objects.filter(status=1).all()
    video = VideoGallery.objects.filter(status=1).all()
    project_category = ProjectCategory.objects.all()
    publication_category = PubCategory.objects.all()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'subscription was submitted successfully.')
        else:
            messages.error(request, 'Invalid form submission.')

    form = SubscriptionForm()
    context = {
        'photos': photo,
        'videos': video,
        'form': form,
        'project_category': project_category,
        'publication_category': publication_category,
    }
    return render(request, 'gallery.html', context)


class PhotoGalleryDetails(DetailView):
    model = PhotoGallery
    context_object_name = 'photo'
    template_name = 'PhotoGalleryDetail.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoGalleryDetails, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['form'] = SubscriptionForm()
    
        return context

class VideoGalleryDetails(DetailView):
    model = VideoGallery
    context_object_name = 'video'
    template_name = 'VideoGalleryDetail.html'

    def get_context_data(self, **kwargs):
        context = super(VideoGalleryDetails, self).get_context_data(**kwargs)
        context['publication_category'] = PubCategory.objects.all()
        context['project_category'] = ProjectCategory.objects.all()
        context['form'] = SubscriptionForm()
    
        return context
    
def galleryDetails(request, pk):
    photo = PhotoGallery.objects.filter(status=1, pk=id)
    video = VideoGallery.objects.filter(status=1, pk=id)
    
    return render(request, 'galleryDetail.html')