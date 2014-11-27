from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)

    def __unicode__(self):
        return '%s  %s' % (self.name, self.last_name)