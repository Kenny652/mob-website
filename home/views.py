from django.shortcuts import render, get_list_or_404
from django.views import View

# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, 'index.html', {})