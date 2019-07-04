from django.db import models


class SpaceCraft(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=1024, default='', blank=True)

    def __str__(self):
        return self.name
