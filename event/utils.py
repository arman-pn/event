from .models import EventLog

def log_event_action(event, action, metadata=""):
    EventLog.objects.create(
        event=event,
        action=action,
        metadata=metadata
    )
