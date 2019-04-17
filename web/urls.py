from django.urls import path
from web.views import submit_expense

urlpatterns = [
    path('s/', submit_expense)
]
