from django.contrib import admin
from django.contrib.auth.models import Group
from .models import confess,Memes,Feedback,UserPair,Chats,User
from django.urls import path
from django.http import HttpResponse

admin.site.site_header = 'Coding Crew dashboard'
class confessAdmin(admin.ModelAdmin):

    list_display=('subm_text','pub_date','pk','post_muthalali')
    list_filter=('flags','pub_date','claps',)
    change_list_template='admin/confess/confess_change_list.html'

admin.site.register(confess,confessAdmin)
admin.site.register(Memes)
admin.site.register(Chats)
admin.site.register(User)
admin.site.register(UserPair)
admin.site.unregister(Group)
admin.site.register(Feedback)


# Register your models here.
