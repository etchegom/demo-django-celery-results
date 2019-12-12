import json
import uuid
from datetime import timedelta

from celery import shared_task, states
from celery.utils.log import get_task_logger
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django_celery_results.models import TaskResult

from .models import TaskResultJson

logger = get_task_logger(__name__)


@receiver(post_save, sender=TaskResult)
def create_json_result(sender, instance=None, created=False, **kwargs):
    if created:
        result = getattr(instance, "result", None)
        json_result = json.loads(result) if result else {}
        TaskResultJson.objects.create(task_result=instance, json_result=json_result)


STATES = frozenset(
    {states.PENDING, states.RECEIVED, states.STARTED, states.SUCCESS, states.RETRY}
)


@shared_task(name="send_email_to_idle_users")
def send_email_to_idle_users():
    data = []

    idle_time_limit = timezone.now() - timedelta(seconds=settings.IDLE_ELAPSED_TIME_SEC)

    for user in get_user_model().objects.filter(date_joined__lte=idle_time_limit):
        if TaskResult.objects.filter(
            task_name="send_email_to_idle_users",
            json_result__json_result__data__contains=[{"user_id": user.id}],
            status__in=STATES,
        ).exists():
            continue

        content = str(uuid.uuid4())
        # simulate email sending with a simple log
        logger.info("send email to user {}: {}".format(user.id, content))
        data.append({"user_id": user.id, "user_email": user.email, "content": content})

    return dict(data=data)
