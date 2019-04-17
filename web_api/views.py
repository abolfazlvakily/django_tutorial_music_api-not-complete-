from rest_framework import generics
from web.models import Track
from web_api.serializer import musical_serializer
from rest_framework.permissions import IsAuthenticated
from .permissions import OwnerCanManageOrReadOnly


class musical_api_view(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = musical_serializer
    permission_classes = [IsAuthenticated, ]