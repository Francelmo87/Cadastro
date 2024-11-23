from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateField('criado em', auto_now_add=True, auto_now=False)
    modified = models.DateField('modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True                     