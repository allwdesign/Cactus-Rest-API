# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from core.views import TopicViewSet, CactusViewSet


router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'cacti', CactusViewSet)


schema_view = get_swagger_view(title='Docs for CactiAPI')

urlpatterns = [
    url(r'^docs/', schema_view)
]

urlpatterns += router.urls