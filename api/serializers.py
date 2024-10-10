from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    """serializer for Group object"""
    class Meta:
        model = Group
        fields = ('id', 'name', 'location', 'description')
