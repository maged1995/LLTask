from django.urls import path
from receipt_processor import views

urlpatterns = [
    path('receipts/', views.receipt_list)
]