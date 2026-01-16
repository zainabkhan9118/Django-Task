"""Django admin configuration for polls."""
from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    """Inline admin interface for choices."""

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Admin interface for questions."""

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}
         ),
    ]
    list_display = ("question_text", "pub_date", "was_published_recently")
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
