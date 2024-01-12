from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.category)
admin.site.register(models.item)

