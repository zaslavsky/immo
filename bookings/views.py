# bookings/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.http import HttpResponseRedirect
from .models import Booking

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Теперь request.user гарантированно авторизован
        return Booking.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if 'cancel_booking' in request.POST:
            booking_id = request.POST.get('cancel_booking')
            booking = get_object_or_404(Booking, id=booking_id, user=request.user)
            if booking.start_date > now().date():
                booking.status = 'cancelled'
                booking.save()
        return HttpResponseRedirect(request.path)

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['listing', 'start_date', 'end_date', 'comments']  # Статус выставляется по умолчанию
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
