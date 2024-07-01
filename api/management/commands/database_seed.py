from django.core.management.base import BaseCommand
from .seed_roles import Command as roleSeeder


class Command(BaseCommand):
    help = "Seed the database with initial table's data"
    
    def handle(self, *args, **kwargs):
        roleSeeder.handle(self=self)