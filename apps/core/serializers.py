# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cactus, Topic

class UserSerializer(serializers.ModelSerializer):
    # is a reverse relationship on the User model
    cacti = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Cactus.objects.all())
    topics = serializers.PrimaryKeyRelatedField(many=True,
                                                 queryset=Topic.objects.all())

    class Meta:
        model = User
        # These fields must be returned to the API from the User model.
        fields = ('id', 'username', 'cacti', 'topics',)

class CactusSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Cactus
        fields = ('id', 'name', 'owner',)

class TopicSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    cactus_id = serializers.PrimaryKeyRelatedField(
        queryset=Cactus.objects.all(),
        write_only=True,
        source='cactus',
    )
    cactus = CactusSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = (
            'id',
            'title',
            'content',
            'date_added',
            'cactus',
            'cactus_id',
            'owner',
        )
