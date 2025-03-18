from django.contrib import admin
from .models import Event, EventMembership, EventLog

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator')
    search_fields = ('name',)

admin.site.register(Event, EventAdmin)

class EventMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'joined_at')
    search_fields = ('user__username', 'event__name')

admin.site.register(EventMembership, EventMembershipAdmin)

class EventLogAdmin(admin.ModelAdmin):
    list_display = ('event', 'action', 'timestamp')
    search_fields = ('event__name', 'action')
    list_filter = ('timestamp',)

admin.site.register(EventLog, EventLogAdmin)
