from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Event, EventMembership, EventLog
from .serializers import EventSerializer, EventLogSerializer

# Event View (GET, POST, PUT, DELETE operations for Event)
class EventView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id=None):
        if event_id:
            try:
                event = Event.objects.get(id=event_id)
                serializer = EventSerializer(event)
                return Response(serializer.data)
            except Event.DoesNotExist:
                return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)  # Assume the user is the creator
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        event.delete()
        return Response({"message": "Event deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# Event Membership View (POST to join an event)
class EventMembershipView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if user is already a member
        if EventMembership.objects.filter(user=request.user, event=event).exists():
            return Response({"error": "You are already a member of this event."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if event has reached capacity
        if event.members.count() >= event.capacity:
            return Response({"error": "Event is full."}, status=status.HTTP_400_BAD_REQUEST)

        membership = EventMembership.objects.create(user=request.user, event=event)
        return Response({"message": "You have successfully joined the event."}, status=status.HTTP_201_CREATED)


# Event Log View (GET logs for a specific event)
class EventLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id=None):
        if event_id:
            logs = EventLog.objects.filter(event_id=event_id)
            serializer = EventLogSerializer(logs, many=True)
            return Response(serializer.data)
        else:
            logs = EventLog.objects.all()
            serializer = EventLogSerializer(logs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = EventLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Event Members View (GET members of a specific event)
class EventMembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the request user is the creator
        if event.creator != request.user:
            return Response({"error": "You are not authorized to view members."}, status=status.HTTP_403_FORBIDDEN)

        members = EventMembership.objects.filter(event=event)
        member_usernames = [membership.user.username for membership in members]
        return Response({"members": member_usernames})
