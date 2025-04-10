from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Listing
from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.models import Group
from bookings.forms import BookingForm
from bookings.models import Booking
from django.db.models import Q
from django.core.paginator import Paginator

class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listing_list.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['listings'], 2) 
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listings/listing_detail.html'
    context_object_name = 'listing'

class ListingCreateView(CreateView):
    model = Listing
    fields = ['title', 'description', 'location', 'price', 'rooms', 'property_type']
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listing-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ListingUpdateView(UpdateView):
    model = Listing
    fields = ['title', 'description', 'location', 'price', 'rooms', 'property_type', 'status']
    template_name = 'listings/listing_form.html'
    success_url = reverse_lazy('listing-list')

class ListingDeleteView(DeleteView):
    model = Listing
    template_name = 'listings/listing_confirm_delete.html'
    success_url = reverse_lazy('listing-list')

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    reviews = listing.reviews.all()
    review_form = ReviewForm()
    booking_form = BookingForm()
    booking_success = False
    is_tenant = request.user.role == 'tenant' if request.user.is_authenticated else False
    is_landlord = request.user.role == 'landlord' if request.user.is_authenticated else False

    # Обработка бронирования для tenant
    if request.method == 'POST' and 'book_submit' in request.POST and is_tenant:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.listing = listing
            booking.user = request.user
            booking.save()
            booking_success = True

    # Обработка отклонения бронирования для landlord
    if request.method == 'POST' and 'reject_booking' in request.POST and is_landlord:
        booking_id = request.POST.get('reject_booking')
        booking = get_object_or_404(Booking, id=booking_id, listing=listing, listing__owner=request.user)
        booking.status = 'cancelled'
        booking.save()

    # Обработка подтверждения бронирования для landlord
    if request.method == 'POST' and 'confirm_booking' in request.POST and is_landlord:
        booking_id = request.POST.get('confirm_booking')
        booking = get_object_or_404(Booking, id=booking_id, listing=listing, listing__owner=request.user)
        booking.status = 'confirmed'
        booking.save()

    # Получение бронирований для landlord
    landlord_bookings = None
    if is_landlord:
        landlord_bookings = Booking.objects.filter(listing=listing, listing__owner=request.user)

    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'reviews': reviews,
        'review_form': review_form,
        'booking_form': booking_form,
        'booking_success': booking_success,
        'is_tenant': is_tenant,
        'is_landlord': is_landlord,
        'landlord_bookings': landlord_bookings,
    })