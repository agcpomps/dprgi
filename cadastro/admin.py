from django.contrib import admin

# Register your models here.
from . models import Morador, Habitacao

admin.site.register(Morador)
admin.site.register(Habitacao)
