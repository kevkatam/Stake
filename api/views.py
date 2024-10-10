from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GroupSerializer
from .models import Group

# Create your views here.
class GroupViewset(viewsets.ModelViewSet):
    """viewset for Group object's endpoint """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
