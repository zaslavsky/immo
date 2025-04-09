from django.db import models
from django.conf import settings
from listings.models import Listing

class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='search_history',
                             on_delete=models.CASCADE, null=True, blank=True)
    query = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username if self.user else self.query

class ListingViewLog(models.Model):
    listing = models.ForeignKey(Listing, related_name='view_logs', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='view_logs',
                             on_delete=models.SET_NULL, null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.listing.title} viewed at {self.viewed_at}"
