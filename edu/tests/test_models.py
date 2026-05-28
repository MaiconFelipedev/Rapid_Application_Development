from django.test import TestCase
from edu.models import Autor


class AutorModelTest(TestCase):
    def test_str_autor(self):
        autor = Autor.objects.create(nome="Machado de Assis")

        self.assertEqual(str(autor), "Machado de Assis")