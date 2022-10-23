from django.contrib import admin
from .models import NewsDB
from .models import SchedulsDB
from .models import LattersToRector

admin.site.register(NewsDB)
admin.site.register(SchedulsDB)
admin.site.register(LattersToRector)

