from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    # Grouping fields
    # fieldsets = (
    #   ("П.І.П", {
    #       'fields': ('surname', 'name', 'last_name',),
    #    }),
    # )

    search_fields = ['name', 'surname', 'last_name']


admin.site.register(Profile, ProfileAdmin)
