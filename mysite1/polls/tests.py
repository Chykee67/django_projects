import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_recently_published_with_future_question(self):
        """
        Test to see that was_recently_published() returns False for questions with pub_date in the future
        """
        future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=10))

        self.assertIs(future_question.was_recently_published(), False)

    def test_was_recently_published_with_old_question(self):
        """
        Test to see that was_recently_published() returns False for questions with pub_date older than 1 day
        """
        old_question = Question(pub_date=timezone.now() - datetime.timedelta(days=1, seconds=1))

        self.assertIs(old_question.was_recently_published(), False)

    def test_was_recently_published_with_recent_question(self):
        """
        Test to see that was_recently_published() returns True for questions with pub_date within the past day
        """
        recent_question = Question(pub_date=timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59))

        self.assertIs(recent_question.was_recently_published(), True)

def create_question(text, days):
    """
    function for creating a Question object using a given question text and pub_date defined by days relative to timezone.now()
    """
    return Question.objects.create(question_text=text, pub_date=timezone.now() + datetime.timedelta(days=days))


class IndexViewTests(TestCase):
    """Test IndexView responses for different question scenarios"""

    def test_no_question(self):

        """ Test to see that appropriate message is displayed when no questions are available"""

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest'], [])
    
    def test_past_question(self):

        """ Test to see that questions with pub_date in the past are displayed on the index page. """

        question = create_question(text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest'], [question])

    def test_future_question(self):
        """ Test to see that questions with future pub_dates are not published on index page. """

        question = create_question(text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest'], [])

    def test_future_and_past_questions(self):

        """ Test to to see that only past question is published """

        question1 = create_question(text="Past question.", days=-30)
        question2 = create_question(text="Future question. ", days=30)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest'], [question1])

    def test_multiple_past_questions(self):

        """ Test to see that more than one past question is published """

        question1 = create_question(text="Past question 1. ", days=-25)
        question2 = create_question(text="Past question 2. ", days=-15)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest'], [question1, question2])