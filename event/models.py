from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    creator = models.ForeignKey(User, related_name="created_events", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('closed', 'Closed')])

    def __str__(self):
        return self.name


class EventMembership(models.Model):
    user = models.ForeignKey(User, related_name="memberships", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="members", on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'event']




class EventLog(models.Model):
    event = models.ForeignKey(Event, related_name="logs", on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.CharField(max_length=255,blank=False)

    def __str__(self):
        return f"{self.action} at {self.timestamp}"


