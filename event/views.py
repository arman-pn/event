from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .serializers import EventSerializer


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Event, EventMembership

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import EventLog
from .serializers import EventLogSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Event, EventMembership



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]



class EventMembershipView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)

        if EventMembership.objects.filter(user=request.user, event=event).exists():
            return Response({"error": "You are already a member of this event."}, status=status.HTTP_400_BAD_REQUEST)

        if event.members.count() >= event.capacity:
            return Response({"error": "Event is full."}, status=status.HTTP_400_BAD_REQUEST)

        membership = EventMembership.objects.create(user=request.user, event=event)
        return Response({"message": "You have successfully joined the event."}, status=status.HTTP_201_CREATED)



class EventLogViewSet(viewsets.ModelViewSet):
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        if event_id:
            return EventLog.objects.filter(event_id=event_id)
        return EventLog.objects.all()


class EventMembersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        if event.creator != request.user:
            return Response({"error": "You are not authorized to view members."}, status=403)

        members = EventMembership.objects.filter(event=event)
        member_usernames = [membership.user.username for membership in members]
        return Response({"members": member_usernames})

























































# from rest_framework import viewsets, status
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from .models import Event, EventMembership
# from .serializers import EventSerializer, EventMembershipSerializer


# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)

#     @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
#     def join(self, request, pk=None):
#         event = self.get_object()

#         if event.status == 'CLOSED':
#             return Response({'error': 'This event is closed.'}, status=status.HTTP_400_BAD_REQUEST)

#         if event.memberships.count() >= event.capacity:
#             return Response({'error': 'Event is full.'}, status=status.HTTP_400_BAD_REQUEST)

#         membership, created = EventMembership.objects.get_or_create(event=event, user=request.user)
#         if not created:
#             return Response({'error': 'You are already a member of this event.'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = EventMembershipSerializer(membership)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class EventMembershipViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = EventMembership.objects.all()
#     serializer_class = EventMembershipSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
