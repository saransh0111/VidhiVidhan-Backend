from django.urls import path
from .views import CustomerViewSet
from users.views import *

urlpatterns = [
    path('send-otp/', SendOTP.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify-otp'), 
    path('resend-otp/', ResendOTP.as_view(), name='resend-otp'), 
    path('get-user-profile/', GetUserProfileAPI.as_view(), name="get-user-profile"),
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('customers/int:pk/', CustomerViewSet.as_view({'get': 'retrieve'}), name='customer-detail'),
    path('all-shop-list/', ListShopsAPIView.as_view(), name="All shop List API"),
    path('all-pandit-list/', ListPanditsAPIView.as_view(), name="All Pandit List API"),
]