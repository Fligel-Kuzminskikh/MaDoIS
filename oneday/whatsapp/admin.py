from django.contrib import admin
from .models import Case, Found, News


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "active", ]
    list_filter = ["user", "active", ]


@admin.register(Found)
class FoundAdmin(admin.ModelAdmin):
    list_display = ["case", "text", "created", ]
    list_filter = ["case", ]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["case", "oldtext", "newtext", "created", ]
    list_filter = ["case", ]
