import pytest
from django.utils import timezone

from polls.models import Question


# Testes com acesso a banco de dados
@pytest.mark.django_db
def test_question_was_published_recently_success():
    # Given
    question_text = 'Qual sua linguagem de programação favorita?'
    pub_date = timezone.now()
    active = True

    # When
    # Ambiente de testes não persistem dados no banco
    question = Question.objects.create(
        question_text=question_text, pub_date=pub_date, active=active
    )

    # Then
    assert question.was_published_recently() is True
