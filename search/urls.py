from django.urls import path
from .views import ListingSearchView, search_history

urlpatterns = [
    path('listings/', ListingSearchView.as_view(), name='listing-search'),
    path('history/', search_history, name='search-history'),
]
