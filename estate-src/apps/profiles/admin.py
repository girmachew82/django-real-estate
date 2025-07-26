from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","pkid","user","sex","phone_number","country","city"]
    list_filter = ['sex','country','city']
    list_display_links =['id','pkid','user']


admin.site.register(Profile, ProfileAdmin)