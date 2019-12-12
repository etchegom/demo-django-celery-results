from django.contrib.postgres.fields import JSONField
from django.db import models
from django_celery_results.models import TaskResult


class TaskResultJson(models.Model):
    class Meta:
        db_table = "task_result_json"

    task_result = models.OneToOneField(TaskResult, related_name="json_result", on_delete=models.CASCADE)
    json_result = JSONField()
