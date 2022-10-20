from app.models import Employee, Subdivision
from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
import random


class Command(BaseCommand):
    help = 'Seeder db'


    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Employee, 42762, {
            'fio': lambda x: seeder.faker.first_name() + seeder.faker.last_name(),
            'salary': lambda x: random.randint(50000, 1000000),
            'subdivision_id': lambda x: random.randint(1, 25),
            'position': lambda x: seeder.faker.sentence(),
            'date_coming': lambda x: seeder.faker.date(),
        })

        seeder.add_entity(Subdivision, 10, {
            'name': lambda x: seeder.faker.sentence(),
            'parent_subdivision_id': lambda x: random.randint(1, 10),
        })

        seeder.execute()
