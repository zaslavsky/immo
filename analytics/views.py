from django.views.generic import ListView, CreateView
from .models import SearchHistory, ListingViewLog
from django.urls import reverse_lazy

class SearchHistoryListView(ListView):
    model = SearchHistory
    template_name = 'analytics/search_history_list.html'
    context_object_name = 'histories'

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)

class ListingViewLogListView(ListView):
    model = ListingViewLog
    template_name = 'analytics/listing_view_log_list.html'
    context_object_name = 'view_logs'
