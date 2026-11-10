from unittest.mock import Base

from django.core.management.base import BaseCommand
import uvicorn

class Command(BaseCommand):
    help = "Run the django application with uvicorn"
    def handle(self, *args, **options):
        uvicorn.run('Ch70.asgi:application', host="127.0.0.1", port=8000, reload=True)