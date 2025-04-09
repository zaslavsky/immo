# bookings/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Booking

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        # Теперь request.user гарантированно авторизован
        return Booking.objects.filter(user=self.request.user)

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['listing', 'start_date', 'end_date']  # Статус выставляется по умолчанию
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
