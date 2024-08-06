from django.urls import path
from rest_framework.routers import DefaultRouter

from reviews.views.reviews_view import ReviewsViewSet

router = DefaultRouter()

urlpatterns = [
    path(
        'reviews/<uuid:book_id>/',
        ReviewsViewSet.as_view(
            {
                'post': 'submit',
                'patch': 'resubmit',
            }
        ),
        name='reviews'
    ),
]
