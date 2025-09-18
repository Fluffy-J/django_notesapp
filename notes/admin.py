from django.contrib import admin

from .models import Title, Body , Category


admin.site.site_header = "Notes Admin"
admin.site.site_title = "Notes Admin Area"
admin.site.index_title = "Welcome to the Notes Admin"

class BodyTextInline(admin.TabularInline):
    model = Body
    extra = 1

# class CategoryTextInline(admin.TabularInline):
#     model = Category
#     extra = 0

class TitleAdmin(admin.ModelAdmin):
     fieldsets = [(None, {'fields': ['title_text']}),]
     inlines = [BodyTextInline]

admin.site.register(Title, TitleAdmin)
admin.site.register(Category)

