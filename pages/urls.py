from django.urls import path
from .views import homePageView, aboutPageView, brianPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('brian/', brianPageView, name='brian'),
    path('homePost/', homePost, name='homePost'),
path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
