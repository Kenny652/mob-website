from django.shortcuts import render, get_list_or_404
from django.views import View

# Create your views here.
def home_page(request, *args, **kwargs):
    return render(request, 'index.html', {})

def ja_info(request, *args, **kwargs):
    return render(request, 'ja-info.html', {})

def ministeres_info(request, *args, **kwargs):
    return render(request, 'ministere-info.html', {})

def a_propos(request, *args, **kwargs):
    return render(request, 'a-propos.html', {})