from datetime import timedelta

from django.db import models
from django.utils import timezone

# Create your models here.


# Criando os modelos do ORM
# ./manage.py makemigrations para criar migration e ./manage.py migrate para realizar upgrade
# ./manage.py migrate polls para especificar app
class Question(models.Model):
    question_text = models.CharField('Texto da questão', max_length=200)
    pub_date = models.DateTimeField('Data publicado')
    active = models.BooleanField('Ativo', default=True)
    # Campo que não aceita nulos por padrão é necessário default, Django propõe soluções automáticas para o erro quando executado.
    x = models.TextField(default='')
    # Rollback: ./manage.py migrate polls 0002

    class Meta:
        # Alterando metadados, verbose_name para nome usado na template
        # Traduzindo templates
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

    def __str__(self):
        # Usado para representar os objetos, caso contrário é retornado <Question: Question object (n)>
        return f'{self.id}: {self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name='Questão'
    )
    choice_text = models.CharField('Texto da escolha', max_length=200)
    votes = models.IntegerField('Votos', default=0)

    class Meta:
        verbose_name = 'Escolha'
        verbose_name_plural = 'Escolhas'

    def __str__(self):
        return f'{self.id}: {self.choice_text}'


# Usando o shell para manipular os modelos: ./manage.py shell. Use o módulo ipython para melhor interface

# from polls.models import Question, Choice
# from django.utils import timezone

# q = Question(question_text='Pergunta', pub_date=timezone.now())
# q.save()
# q.id, q.question_text

# q = Question.objects.all()
# Question.objects.filter(active=True)

# q[0].question_text = 'O que é Django?'
# q.save()

# Questions.objects.get(id=1)
# Questions.objects.first()
# c = Choice(question=Question.objects.get(id=1), choice_text='Django é um framework de desenvolvimento web...')
# c.save()

# Question.objects.get(question_text__icontains='Django')
# Question.objects.update(), .delete(), ...
