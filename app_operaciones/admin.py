from django.contrib import admin
from .models import Mascota, Sala

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
  pass

class SalaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Sala, SalaAdmin)