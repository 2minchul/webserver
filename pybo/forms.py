from django import forms
from django.db.models import TextChoices

from pybo.models import Question, Answer, Comment


class PostDetailRequestQuery(forms.Form):
    class AnswerOrder(TextChoices):
        RECENT = 'recent', '최신순'
        RECOMMEND = 'recommend', '추천순'

    answer_page = forms.IntegerField(required=False)
    answer_order = forms.ChoiceField(
        choices=AnswerOrder.choices,
        required=False,
    )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
