from django.test import TestCase

from edu.models import Autor
from edu.serializers import AutorSerializer


class AutorSerializerTest(TestCase):
    def test_autor_serializer(self):
        autor = Autor.objects.create(nome="C. S. Lewis")
        serializer = AutorSerializer(autor)

        self.assertEqual(serializer.data['nome'], "C. S. Lewis")