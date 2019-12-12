import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_results.models import TaskResult

from .models import TaskResultJson


@receiver(post_save, sender=TaskResult)
def create_json_result(sender, instance=None, created=False, **kwargs):
    if created:
        result = getattr(instance, "result", None)
        json_result = json.dumps(result) if result else {}
        TaskResultJson.objects.create(task_result=instance, json_result=json_result)
