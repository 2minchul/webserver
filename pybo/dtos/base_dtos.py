from typing import Iterable, Optional

from django.core.paginator import Page

from common.dtos import ContextDto
from pybo.forms import AnswerForm
from pybo.models import Question, Answer


class BaseContext(ContextDto):
    pass


class PostDetail(BaseContext):
    question: Question
    answer_page: Page
    answer_count: int
    answer_list: Iterable[Answer]
    answer_form: Optional[AnswerForm]
