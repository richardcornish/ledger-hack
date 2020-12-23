from django.contrib import admin

from .models import Victim


class VictimAdmin(admin.ModelAdmin):
    list_filter = ('newsletter',)
    readonly_fields = ('reference_id',)
    search_fields = ['email']


admin.site.register(Victim, VictimAdmin)
