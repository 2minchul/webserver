from django.contrib.auth.models import User
from django.core.paginator import Page
from django.db.models import QuerySet

from pybo.dtos import BaseContext
from pybo.models import Question, Answer, Comment


class UserProfile(BaseContext):
    user: User
    post: QuerySet[Question]
    post_page: Page
    answer: QuerySet[Answer]
    answer_page: Page
    comment: QuerySet[Comment]
    comment_page: Page
