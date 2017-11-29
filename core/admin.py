from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Cactus, Topic

admin.site.register(Cactus)
admin.site.register(Topic)

TokenAdmin.raw_id_fields = ('user',)