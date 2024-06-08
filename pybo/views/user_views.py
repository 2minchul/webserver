from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from pybo.dtos import UserProfile
from pybo.models import Question, Answer, Comment


def user_profile(request, user_id: int):
    limit = 10
    user = get_object_or_404(User, pk=user_id)

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
    context = {'profile': profile}

    return render(request, 'pybo/user_profile.html', context)
