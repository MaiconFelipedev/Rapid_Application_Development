from rest_framework.test import APITestCase
from rest_framework import status

from edu.models import Autor


class AutorAPITest(APITestCase):
    def test_criar_autor_api(self):
        data = {
            "nome": "Autor Teste API"
        }

        response = self.client.post(
            "/edu/api/autores/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Autor.objects.count(), 1)
        self.assertEqual(Autor.objects.first().nome, "Autor Teste API")