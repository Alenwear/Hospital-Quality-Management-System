from django.contrib import admin
from .models import AgentInfo, CheInfo, AdmInfo

# Register your models here.

admin.site.register(AgentInfo)
admin.site.register(CheInfo)
admin.site.register(AdmInfo)
