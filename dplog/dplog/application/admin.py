from django.contrib import admin
from .models import Application, Client, ClientAddress, ClientPerson, Status, Store


class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(Application, ApplicationAdmin)


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(Client, ClientAdmin)


class ClientPersonAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(ClientPerson, ClientPersonAdmin)


class ClientAddressAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(ClientAddress, ClientAddressAdmin)


class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(Status, StatusAdmin)


class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ['pk']


admin.site.register(Store, StoreAdmin)
