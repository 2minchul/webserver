from django.contrib import admin

from .models import Question, Category, Answer, Comment


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']
