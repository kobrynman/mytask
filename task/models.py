from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(
        max_length=80,
        validators=[
            RegexValidator(
                r'^\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                'Only (XXX)XXX-XX-XX are allowed.',
            )
        ],
    )
    def __unicode__(self):
        return '%s  %s' % (self.name, self.last_name)