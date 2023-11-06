from django.urls import path
from .views import CustomerViewSet

urlpatterns = [
path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
path('customers/int:pk/', CustomerViewSet.as_view({'get': 'retrieve'}), name='customer-detail'),
]