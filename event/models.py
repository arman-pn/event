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
    metadata = models.JSONField()

    def __str__(self):
        return f"{self.action} at {self.timestamp}"








































































# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Event(models.Model):
#     STATUS_CHOICES = [
#         ('OPEN', 'Open'),
#         ('CLOSED', 'Closed')
#     ]

#     creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     capacity = models.PositiveIntegerField()
#     status = models.CharField(max_length=6, choices=STATUS_CHOICES, default='OPEN')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class EventMembership(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='memberships')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_memberships')
#     joined_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('event', 'user')

#     def __str__(self):
#         return f'{self.user.username} - {self.event.name}'
