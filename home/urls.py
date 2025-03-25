from django.urls import path
from .views import home_page, ja_info, ministeres_info, a_propos

app_name = 'home'

urlpatterns = [
    path('', home_page, name='home-page'),
    path('ja', ja_info, name='ja-info-page'),
    path('ministere', ministeres_info, name='ministere-info-page'),
    path('propos', a_propos, name='a-propos-page'),
]
