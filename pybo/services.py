from typing import Optional

from django.core.paginator import Paginator
from django.db.models import Count

from pybo.dtos import PostDetail
from pybo.forms import AnswerForm, PostDetailRequestQuery
from pybo.models import Question


def retrieve_post_detail(question: Question, params: PostDetailRequestQuery, answer_form: Optional[AnswerForm] = None,
                         answer_page_limit: int = 5) -> PostDetail:
    answer_page = params.cleaned_data.get('answer_page', 1)
    answer_order = params.cleaned_data.get('answer_order', PostDetailRequestQuery.AnswerOrder.RECENT)

    answer_qs = question.answer_set
    answer_count = answer_qs.count()
    if answer_order == PostDetailRequestQuery.AnswerOrder.RECOMMEND:
        answer_qs = answer_qs.annotate(votes=Count('voter')).order_by('-votes', 'create_date')
    else:  # recent
        answer_qs = answer_qs.order_by('create_date')

    paginator = Paginator(answer_qs, answer_page_limit)

    page = paginator.get_page(answer_page)

    return PostDetail(
        question=question,
        answer_count=int(answer_count),
        answer_page=page,
        answer_list=list(page.object_list),
        answer_form=answer_form,
    )
