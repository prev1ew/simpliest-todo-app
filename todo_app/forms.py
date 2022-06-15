from .models import ToDoItem
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, DateTimeInput
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class ToDoItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            'title',
            'description',
            'priority',
            'due_date',
            'is_completed'
        ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input title'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input description'
            }),
            "is_complete": CheckboxInput(),
            "due_date": DateTimeInput(attrs={
                'id': 'datetimepicker',
                'type': 'text'
            })
        }
