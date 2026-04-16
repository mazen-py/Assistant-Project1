from django.db import models

class Task(models.Model):
    TASK_TYPES = (
        ('DAILY', 'Daily Task'),
        ('PLANNED', 'Planned Task'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    task_type = models.CharField(max_length=10, choices=TASK_TYPES)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    warning_triggered = models.BooleanField(default=False)

    def __str__(self):
        return self.title