from django.contrib import admin

from .models import Flat, Complaint, Own


class OwnersInline(admin.TabularInline):
    model = Own.flat.through
    raw_id_fields = ('own',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnersInline,
    ]


admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat',)


admin.site.register(Complaint, ComplaintAdmin)


class OwnAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    search_fields = ('owner',)


admin.site.register(Own, OwnAdmin)