from django.contrib import admin
from drama_datas.models import DramaData, Company, Actor, Cast

# Register your models here.
admin.site.register(DramaData)
admin.site.register(Company)
admin.site.register(Actor)
admin.site.register(Cast)