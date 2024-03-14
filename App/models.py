from django.db import models

class NetworkTraffic(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    source_ip = models.CharField(max_length=50)
    destination_ip = models.CharField(max_length=50)
    protocol = models.CharField(max_length=20)

class SecurityEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    event_type = models.CharField(max_length=50)
    description = models.TextField()
