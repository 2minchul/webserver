from django.contrib import admin

from .models import Question, Category


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
