from django.core.management.base import BaseCommand
from main.models import Tab, ContentBlock

class Command(BaseCommand):
    help = 'Populate the database with default data'

    def handle(self, *args, **kwargs):
        # Создайте или получите вкладку
        tab, created = Tab.objects.get_or_create(
            slug="default-tab",
            defaults={
                "name": "Default Tab",
                "order": 0,
                "is_active": True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created new Tab: Default Tab'))
        else:
            self.stdout.write(self.style.WARNING('Tab "Default Tab" already exists'))

        # Создайте блок контента
        content_block, created = ContentBlock.objects.get_or_create(
            tab=tab,
            block_type="carousel",
            defaults={
                "order": 0,
                "title": "Default Content Block"
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created new ContentBlock: Default Content Block'))
        else:
            self.stdout.write(self.style.WARNING('ContentBlock already exists for Default Tab'))
