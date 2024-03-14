from django.contrib import admin

# Register your models here.
from .models import Herb, Planet

admin.site.register(Herb)
admin.site.register(Planet)