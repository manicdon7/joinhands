from django.contrib import admin
from .models import Res,Sign
# Register your models here.
@admin.register(Res)
class RestaurantAdmin(admin.ModelAdmin):
    res_display = ('name','desc','image')
@admin.register(Sign)
class SAdmin(admin.ModelAdmin):
    signup_display = ('user','password','designation')

