from django.core.management.base import BaseCommand
from program.models import User

class Command(BaseCommand):
    help = "Update user address by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('address', type=str, help='User address')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        address = kwargs.get('address')
        user = User.objects.filter(pk=pk).first()
        user.address = address
        user.save()
        self.stdout.write(f'{user}')