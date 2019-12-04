# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Generating Tokens"""
    if created:
        Token.objects.create(user=instance)


class Cactus(models.Model):
    """Cactus model"""
    # User that created current cactus
    owner = models.ForeignKey('auth.User', related_name='cacti',
                              on_delete=models.CASCADE)
    # Flower name
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Cactus"
        verbose_name_plural = "Cacti"

    def __str__(self):
        return self.name


class Topic(models.Model):
    """Topic about Cactus"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    cactus = models.ForeignKey(Cactus, on_delete=models.CASCADE)
    # User that created current topic
    owner = models.ForeignKey('auth.User', related_name='topics',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self):
        return '%s \n\n %s' % (self.title, self.content)
