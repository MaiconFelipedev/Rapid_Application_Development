from decimal import Decimal
import random

from django.core.management.base import BaseCommand
from faker import Faker

from edu.models import Livro, Editora


class Command(BaseCommand):
    help = 'Gera 100 livros fictícios usando Faker'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        # garante que exista pelo menos uma editora
        editoras = list(Editora.objects.all())

        if not editoras:
            editoras = [
                Editora.objects.create(nome='Companhia das Letras'),
                Editora.objects.create(nome='Editora Abril'),
                Editora.objects.create(nome='Saraiva'),
                Editora.objects.create(nome='Record'),
                Editora.objects.create(nome='Atlas'),
            ]

        total_criados = 0

        while total_criados < 100:
            isbn = fake.isbn13(separator='')

            # evita erro de ISBN duplicado
            if Livro.objects.filter(isbn=isbn).exists():
                continue

            titulo = fake.sentence(nb_words=4).replace('.', '')
            publicacao = fake.date_between(start_date='-10y', end_date='today')
            preco = Decimal(str(round(random.uniform(20, 150), 2)))
            estoque = random.randint(1, 100)
            editora = random.choice(editoras)

            Livro.objects.create(
                isbn=isbn,
                titulo=titulo,
                publicacao=publicacao,
                preco=preco,
                estoque=estoque,
                editora=editora
            )

            total_criados += 1

        self.stdout.write(self.style.SUCCESS('100 livros criados com sucesso!'))