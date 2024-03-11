from django.core.management.base import BaseCommand
from program.models import User

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', 
                    age=25,
                    email='john@example.com', 
                    phone='89274104636',
                    address='Russia, Kazan, Lenina st., 1',
                    password='secret')
        user.save()
        self.stdout.write(f'{user}')