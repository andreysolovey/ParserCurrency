from django.contrib import admin
from scraping.models import *


admin.site.register(Job, admin.ModelAdmin)
