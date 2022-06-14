from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoItem(models.Model):

    class Priority(models.TextChoices):
        HIGH = 'High', _('High')
        MEDIUM = 'Medium', _('Medium')
        LOW = 'Low', _('Low')

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    priority = models.CharField(
        max_length=30,
        choices=Priority.choices,
        default=Priority.MEDIUM)

    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    is_completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date.ctime()}"

    class Meta:
        ordering = ["-priority", "due_date"]
