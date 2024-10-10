from django.urls import path, include
from .views import GroupViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', GroupViewset)

urlpatterns = [
    path('', include(router.urls)),
]
