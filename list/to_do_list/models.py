from django.db import models

class Things(models.Model):
    name_task = models.CharField(max_length=150)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.name_task