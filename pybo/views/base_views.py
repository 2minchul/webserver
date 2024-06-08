from functools import lru_cache

from django.core.exceptions import BadRequest
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from pybo.forms import PostDetailRequestQuery
from pybo.models import Question, Category
from pybo.services import retrieve_post_detail, increase_view_count


@lru_cache(maxsize=1)
def _get_default_category():
    return Category.objects.first().name


def index(request):
    return redirect('pybo:list', category=_get_default_category())


def list_post(request, category: str):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    question_qs = Question.objects.filter(category__name=category)
    question_qs = question_qs.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_qs, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'category': category}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    params = PostDetailRequestQuery(request.GET)
    if not params.is_valid():
        raise BadRequest("Invalid request query")

    question = get_object_or_404(Question, pk=question_id)
    increase_view_count(question_id)
    post_detail = retrieve_post_detail(question, params)
    context = {'post': post_detail}
    return render(request, 'pybo/question_detail.html', context)
