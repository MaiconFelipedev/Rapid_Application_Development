from django.test import TestCase

from edu.forms import AutorForm


class AutorFormTest(TestCase):
    def test_autor_form_valido(self):
        form = AutorForm(data={
            'nome': 'Ariano Suassuna'
        })

        self.assertTrue(form.is_valid())