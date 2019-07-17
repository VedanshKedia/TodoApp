from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

POSSIBLE_STATUSES = (
    ('Completed', 'Completed'),
    ('Incomplete', 'Incomplete')
)


class TodoListItem(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    todoTitle = models.CharField(max_length=50)
    todoDescription = models.CharField(max_length=400)
    todoDateTime = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='High')
    status = models.CharField(max_length=10, choices=POSSIBLE_STATUSES, default='Incomplete')

    # # Metadata
    # class Meta:
    #     ordering = ['-todoDateTime']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.todoTitle
