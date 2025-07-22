from django.db import models

class Tasks(models.Model):
    title = models.CharField('Exercise', max_length=100)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    