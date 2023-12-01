from django.urls import path
from market.views import ListProductsAPIView


urlpatterns = [
    path('all-products-list/', ListProductsAPIView.as_view(), name="All Rent Out Post List API"),
]
