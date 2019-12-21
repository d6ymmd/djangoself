from django.db import models


class Group(models.Model):
    eland = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name