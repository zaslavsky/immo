from rest_framework import serializers
from .models import SearchHistory, ListingViewLog

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'
        read_only_fields = ['searched_at']

class ListingViewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingViewLog
        fields = '__all__'
        read_only_fields = ['viewed_at']
