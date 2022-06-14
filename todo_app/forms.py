from .models import ToDoItem
from django.forms import ModelForm, TextInput, Textarea


class ToDoItemForm(ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            'title',
            'description',
            'priority',
            'due_date',
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
        }
