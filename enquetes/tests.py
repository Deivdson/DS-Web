import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Pergunta
# Create your tests here.

class PerguntaModeloTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        o método was_published_recently() deve retornar False para questões com data de publicação no futuro
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Pergunta(data_pub=time)
        self.assertIs(future_question.publicado_recentemente(), False)

    def test_was_published_recently_with_old_question(self):
        """
        o método was_published_recently() deve retornar False para questões com data de publicação mais antigas que um dia
        """
        time = timezone.now()-datetime.timedelta(days=1, seconds=1)
        old_question = Pergunta(data_pub=time)
        self.assertIs(old_question.publicado_recentemente(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        o método was_published_recently() deve retornar True para questões com data de publicação inferior a um dia
        """
        time = timezone.now()-datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Pergunta(data_pub=time)
        self.assertIs(recent_question.publicado_recentemente(), True)