from django.contrib import admin

# import your models here
from .models import Crop, Reading, Impact

# Register your models here
admin.site.register(Crop)
admin.site.register(Reading)
admin.site.register(Impact)

