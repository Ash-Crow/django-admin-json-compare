from django.db import models

# Create your models here.


class Stuff(models.Model):
    name = models.CharField(max_length=100)
    json_current = models.JSONField()
    json_new = models.JSONField()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
