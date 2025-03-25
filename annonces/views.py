from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Annonce
from .forms import AnnoncesModelForm

# Create your views here.

class AnnonceCreateView(CreateView):
    template_name = 'annonces/annonce_create.html'
    form_class    = AnnoncesModelForm
    queryset      = Annonce.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    
class AnnonceListView(ListView):
    template_name = 'annonces/annonce_list.html'
    queryset      = Annonce.objects.all()


class AnnonceDetailView(DetailView):
    template_name = 'annonces/annonce_detail.html'
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Annonce, id=id_)


class AnnonceUpdateView(UpdateView):
    template_name = 'annonces/annonce_create.html'
    form_class    = AnnoncesModelForm
    queryset      = Annonce.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Annonce, id=id_)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    

class AnnonceDeleteView(DeleteView):
    template_name = 'annonces/annonce_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Annonce, id=id_)
    
    def get_success_url(self):
        return reverse('annonces:annonce-list')
    
def accueil(request, *args, **kwargs):
    return render(request, 'annonces/annonce_accueil.html', {})