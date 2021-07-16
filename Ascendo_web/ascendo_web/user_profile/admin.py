from django.contrib import admin
from nested_admin import NestedModelAdmin, NestedTabularInline
from csvexport.actions import csvexport
from ascendo_web.game.models import Response
from .models import Profile


class ResponseAdmin(NestedTabularInline):
    model = Response
    fields = ('answer', 'create_date', 'status')
    extra = 0


@admin.register(Profile)
class ProfileAdmin(NestedModelAdmin):
    inlines = [ResponseAdmin]
    search_fields = ['name', 'college', 'nick_name']
    list_display = ['name', 'college']
    list_filter = ['language', 'code', 'has_completed']
    actions = [csvexport]
