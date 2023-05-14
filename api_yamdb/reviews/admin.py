from django.contrib import admin
from .models import Review, Title, Comment, Category, Genre


# admin.site.register(Comment, Review)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    # search_fields = ('name',)
    # list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Genre)
