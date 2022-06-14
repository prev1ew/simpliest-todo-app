import django_tables2 as tables
from .models import ToDoItem


class ToDoItemTable(tables.Table):
    class Meta:
        model = ToDoItem
        template_name = "django_tables2/bootstrap.html"
        fields = ("is_complete", "title", "due_date", "priority")