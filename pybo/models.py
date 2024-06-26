from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    path = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name} (/{self.path})'


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    category = models.ForeignKey('Category', null=False, blank=False, on_delete=models.PROTECT)
    view_count = models.PositiveBigIntegerField(default=0, null=False)

    def __str__(self):
        return self.subject

    @property
    def upvote_count(self) -> int:
        return self.voter.count()


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    @property
    def upvote_count(self) -> int:
        return self.voter.count()

    @property
    def category_name(self) -> str:
        return self.question.category.name


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def category_name(self) -> str:
        if self.question:
            return self.question.category.name
        if self.answer:
            return self.answer.question.category.name
        return ''
