# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework import permissions
from .models import Cactus, Topic
from .serializers import CactusSerializer, TopicSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class TopicViewSet(viewsets.ModelViewSet):
    """
    Topic viewset that provides the standart actions according to user permission
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    # Action .create(), .update(), partial_update() and .destroy() provided
    # only for Authenticated User and cactus owner.
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        # Associated Topic with the user that created them.
        serializer.save(owner=self.request.user)

class CactusViewSet(viewsets.ModelViewSet):
    """
    Cactus viewset that provides the standart actions according to user permission
    """
    queryset = Cactus.objects.all()
    serializer_class = CactusSerializer

    # Action .create(), .update(), partial_update() and .destroy() provided
    # only for Authenticated User and cactus owner.
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        # Associated Cacti with the user that created them.
        serializer.save(owner=self.request.user)
