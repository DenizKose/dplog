from django.contrib import admin
from .models import Profile, ProfileStatus

admin.site.register(ProfileStatus)


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(Profile, ProfileAdmin)
