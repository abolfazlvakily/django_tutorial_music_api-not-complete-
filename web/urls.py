from django.urls import path, include
from web.views import login_form, logout_form, register

urlpatterns = [
    path('', login_form, name='login'),
    path('api/', include('web_api.urls'), name='api'),
    path('exit/', logout_form, name='logout'),
    path('register/', register, name='register'),
]
