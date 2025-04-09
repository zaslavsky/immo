from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Review
from listings.models import Listing
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        listing_id = self.request.GET.get('listing')
        if listing_id:
            return Review.objects.filter(listing_id=listing_id)
        return Review.objects.all()

class ReviewCreateView(CreateView):
    model = Review
    fields = ['listing', 'rating', 'comment']
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
@require_POST
def create_review(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.listing = listing
        review.user = request.user
        review.save()
    return redirect('listing-detail', pk=pk)
