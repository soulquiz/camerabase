from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Event(models.Model):
    event_date = models.DateTimeField('date Event')
    event_pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return str(self.event_date)
