from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api_app import viewsets

router_v1 = routers.DefaultRouter()

router_v1.register(r'users', viewsets.UserViewSet, base_name='user')
router_v1.register(r'information', viewsets.InformationViewSet, base_name='information')

app_name = "api-app"
urlpatterns = [
    url(r'^', include(router_v1.urls)),
]