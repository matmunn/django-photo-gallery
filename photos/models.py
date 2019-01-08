from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.dispatch import receiver


class Photo(models.Model):
    image = models.ImageField()

channel_layer = get_channel_layer()

def send_reset():
    async_to_sync(channel_layer.group_send)('photos', {'type': 'event'})

@receiver(models.signals.post_save, sender=Photo)
def post_save(**kwargs):
    send_reset()

@receiver(models.signals.post_delete, sender=Photo)
def post_delete(**kwargs):
    send_reset()
