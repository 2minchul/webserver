from django.shortcuts import render

from pybo.dtos import History
from pybo.models import Comment, Answer


def recent_history(request):
    limit = 15

    recent_comment = Comment.objects.order_by('-create_date')[:limit]
    recent_answer = Answer.objects.order_by('-create_date')[:limit]

    history = History(
        recent_comment=recent_comment,
        recent_comment_size=len(recent_comment),
        recent_answer=recent_answer,
        recent_answer_size=len(recent_answer),
    )
    context = {'history': history}

    return render(request, 'pybo/recent_history.html', context)
