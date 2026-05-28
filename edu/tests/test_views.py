from django.test import TestCase
from django.urls import reverse

from edu.models import Editora, Livro


class LivroListViewTest(TestCase):
    def setUp(self):
        self.editora = Editora.objects.create(nome="Companhia das Letras")

        Livro.objects.create(
            isbn="1234567890123",
            titulo="Dom Casmurro",
            publicacao="1899-01-01",
            preco=39.90,
            estoque=10,
            editora=self.editora
        )

    def test_livro_list_view_status_code(self):
        response = self.client.get(reverse('livro_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dom Casmurro")