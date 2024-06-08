from typing import Optional

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Count

from pybo.dtos import PostDetail, UserProfile
from pybo.forms import AnswerForm, PostDetailRequestQuery
from pybo.models import Question, Answer, Comment


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


def retrieve_user_profile(user: User, limit: int = 10):
    question_qs = Question.objects.filter(author=user).order_by('-create_date')
    question_page = Paginator(question_qs, limit).get_page(1)

    answer_qs = Answer.objects.filter(author=user).order_by('-create_date')
    answer_page = Paginator(answer_qs, limit).get_page(1)

    comment_qs = Comment.objects.filter(author=user).order_by('-create_date')
    comment_page = Paginator(comment_qs, limit).get_page(1)

    profile = UserProfile(
        user=user,
        post=question_page.object_list,
        post_page=question_page,
        answer=answer_page.object_list,
        answer_page=answer_page,
        comment=comment_page.object_list,
        comment_page=comment_page,
    )
    return profile
