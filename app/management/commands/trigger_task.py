from django.core.management.base import BaseCommand

from app.tasks import send_email_to_idle_users


class Command(BaseCommand):
    help = "Trigger the celery task for testing"

    def handle(self, *args, **options):
        task = send_email_to_idle_users.delay()
        self.stdout.write(
            self.style.SUCCESS("Successfully triggered task {}".format(task.id))
        )
