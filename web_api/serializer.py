from rest_framework import serializers
from web.models import Track


class musical_serializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id','music')
