from django import forms
from .models import PRIORITY_CHOICES, POSSIBLE_STATUSES


class AddNewTodo(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    # datetime = forms.DateTimeField(help_text="Enter Date")
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    status = forms.ChoiceField(choices=POSSIBLE_STATUSES)
