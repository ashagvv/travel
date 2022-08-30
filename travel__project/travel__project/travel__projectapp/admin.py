from django.contrib import admin

# Register your models here.
from .models import places
from .models import highlights
admin.site.register(places)
admin.site.register(highlights)
