from django.contrib import admin

# import your models here
from .models import Crop, Reading, Impact, Photo

# Register your models here
admin.site.register(Crop)
admin.site.register(Reading)
admin.site.register(Impact)
admin.site.register(Photo)

