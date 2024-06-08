from django.db.models import QuerySet

from pybo.dtos import BaseContext
from pybo.models import Comment, Answer


class History(BaseContext):
    recent_comment: QuerySet[Comment]
    recent_comment_size: int
    recent_answer: QuerySet[Answer]
    recent_answer_size: int
