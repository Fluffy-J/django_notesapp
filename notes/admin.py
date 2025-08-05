from django.contrib import admin

from .models import Title, Body

admin.site.site_header = "Notes Admin"
admin.site.site_title = "Notes Admin Area"
admin.site.index_title = "Welcome to the Notes Admin"

class BodyTextInline(admin.TabularInline):
    model = Body
    extra = 0

class TitleAdmin(admin.ModelAdmin):
     fieldsets = [(None, {'fields': ['title_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
     inlines = [BodyTextInline]

admin.site.register(Title, TitleAdmin)

