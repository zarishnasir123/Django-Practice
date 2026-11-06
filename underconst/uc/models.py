from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.
#one row with a tick box: ticked = site shows the under construction page
class UnderConstruction(models.Model):
    is_under_construction = models.BooleanField(default=False)
    uc_duration = models.DateTimeField(
        null=True, blank=True,
        help_text='End date and time of under construction mode. Must be ahead of the server time.',
    )
    uc_note = models.TextField(blank=True)  #message for visitors
    updated_at = models.DateTimeField(auto_now=True)

    #admin calls clean() before saving, so a past end time shows an error on the form
    def clean(self):
        if self.is_under_construction and self.uc_duration and self.uc_duration <= timezone.now():
            raise ValidationError({'uc_duration': 'End date and time must be ahead of the server time.'})

    def __str__(self):
        return 'Under construction' if self.is_under_construction else 'Live'
