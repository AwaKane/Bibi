from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

# Register your models here.
admin.site.register(RendezVous)
admin.site.register(Etablissement)
admin.site.register(User)