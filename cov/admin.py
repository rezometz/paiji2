from django.contrib import admin

# Register your models here.
from cov.models import Covoiturage

class CovoiturageAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'annonce_type', 'good_until', 'notes', 'posted_at')

admin.site.register(Covoiturage, CovoiturageAdmin)