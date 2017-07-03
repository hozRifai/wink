from django.core.management.base import BaseCommand, CommandError
from shortener.models import winkURL 
class Command(BaseCommand):
    help = 'refreshes all winkURL shortcodes '

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options): # *args , **options
        return winkURL.objects.refresh_shortcodes(items=options['items'])