from django.test import TestCase

# Create your tests here.

from .models import Todo
class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        Todo.objects.create(title='Learn python', body='buy course at udemy')

    def test_title_content(self):

        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'Learn python')

    def test_body_content(self):

        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'buy course at udemy')
