from django.contrib import admin
from .models import Room, Reservation, Comment


class ReservationInline(admin.TabularInline):
    model = Reservation
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [ReservationInline]


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation)
admin.site.register(Comment)
