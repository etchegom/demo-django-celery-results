from django.contrib import admin
from django_celery_results.admin import TaskResultAdmin as BaseTaskResultAdmin
from django_celery_results.models import TaskResult

from .models import TaskResultJson

admin.site.unregister(TaskResult)


class TaskResultJsonInline(admin.TabularInline):
    model = TaskResultJson


class TaskResultAdmin(BaseTaskResultAdmin):
    inlines = (TaskResultJsonInline,)


class TaskResultJsonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "json_result",
    )


admin.site.register(TaskResult, TaskResultAdmin)
admin.site.register(TaskResultJson, TaskResultJsonAdmin)
