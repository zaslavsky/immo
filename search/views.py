# search/views.py
from django.views.generic import ListView
from listings.models import Listing
from django.db.models import Q

class ListingSearchView(ListView):
    model = Listing
    template_name = 'search/listing_search.html'
    context_object_name = 'listings'

    def get_queryset(self):
        queryset = Listing.objects.filter(status='active')
        q = self.request.GET.get('q', '')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)
        min_rooms = self.request.GET.get('min_rooms')
        max_rooms = self.request.GET.get('max_rooms')
        if min_rooms:
            queryset = queryset.filter(rooms__gte=min_rooms)
        if max_rooms:
            queryset = queryset.filter(rooms__lte=max_rooms)
        property_type = self.request.GET.get('property_type')
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        ordering = self.request.GET.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
