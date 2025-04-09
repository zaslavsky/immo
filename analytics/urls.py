from django.urls import path
from .views import SearchHistoryListView, ListingViewLogListView

urlpatterns = [
    path('search-history/', SearchHistoryListView.as_view(), name='search-history'),
    path('listing-views/', ListingViewLogListView.as_view(), name='listing-views'),
]
