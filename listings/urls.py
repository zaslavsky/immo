# listings/urls.py
from django.urls import path
from .views import (
    ListingListView, listing_detail,  # Import the function-based view
    ListingCreateView, ListingUpdateView, ListingDeleteView
)
from .views_debug import debug_request

urlpatterns = [
    path('', ListingListView.as_view(), name='listing-list'),
    path('create/', ListingCreateView.as_view(), name='listing-create'),
    path('<int:pk>/', listing_detail, name='listing-detail'),  # Use the function-based view
    path('<int:pk>/update/', ListingUpdateView.as_view(), name='listing-update'),
    path('<int:pk>/delete/', ListingDeleteView.as_view(), name='listing-delete'),
]

urlpatterns += [
    path('debug-request/', debug_request, name='debug-request'),
]
