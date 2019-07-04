from django.contrib import admin
from .models import Tournament,TournamentSeries,TournamentCategory,News,Profile
from tinymce.widgets import TinyMCE
from django.db import models


class TournamentAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tournament_title", "tournament_published"]}),
        ("URL", {"fields": ["tournament_slug"]}),
        ("Series", {"fields": ["tournament_series"]}),
        ("Content", {"fields": ["tournament_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

class NewsAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["news_title", "news_published"]}),
        ("Content", {"fields": ["news_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(TournamentSeries)
admin.site.register(TournamentCategory)
admin.site.register(Tournament,TournamentAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Profile)