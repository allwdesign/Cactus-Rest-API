# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view


from core.views import TopicViewSet, CactusViewSet

app_name = 'core'

schema_view = get_swagger_view(title='Docs for CactiAPI')

router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet, base_name='topics')
router.register(r'cacti', CactusViewSet, base_name='cacti')

urlpatterns = [
	path('', include(router.urls)),
	path('docs/', schema_view),
]