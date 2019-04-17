from django.urls import path
from web_api.views import musical_api_view

urlpatterns = [
    path('', musical_api_view.as_view(), name='musical'),
]
