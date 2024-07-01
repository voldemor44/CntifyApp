from django.core.management.base import BaseCommand
from ...models import Roles


class Command(BaseCommand):
    help = "Seed the database with initial roles"

    def handle(self, *args, **kwargs):
        roles = ["Admin", "User", "Manager", "Developer", "Designer"]

        for role in roles:
            Roles.objects.create(name=role)

        self.stdout.write(self.style.SUCCESS("Roles seeder executed with success..."))
