from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.CustomerProfile)
admin.site.register(models.Address)
