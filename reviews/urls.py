from django.urls import path
from .views import ReviewListView, ReviewCreateView, create_review

urlpatterns = [
    path("", ReviewListView.as_view(), name="review-list"),
    path("create/", ReviewCreateView.as_view(), name="review-create"),
    path('create/<int:pk>/', create_review, name='review-create-fbv'),
]
