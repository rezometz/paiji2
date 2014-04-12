from django.contrib import admin

# Register your models here.
from cov.models import Covoiturage

class CovoiturageAdmin(admin.ModelAdmin):
    list_display = ('id', 'poster', 'annonce_type', 'itinerary', 'dept_datetime', 'ret_datetime')

admin.site.register(Covoiturage, CovoiturageAdmin)
