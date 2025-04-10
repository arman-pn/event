from rest_framework import serializers
from .models import Event, EventMembership, EventLog

class EventSerializer(serializers.ModelSerializer):
    
    creator = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'capacity', 'creator', 'status']
        read_only_fields = ['creator'] 

class EventMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMembership
        fields = ['id', 'user', 'event', 'joined_at']

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLog
        fields = ['event', 'action', 'timestamp', 'metadata']































































# from rest_framework import serializers
# from .models import Event, EventMembership


# class EventSerializer(serializers.ModelSerializer):
#     creator = serializers.ReadOnlyField(source='creator.username')
#     status = serializers.CharField(read_only=True)

#     class Meta:
#         model = Event
#         fields = ['id', 'creator', 'name', 'description', 'location', 'capacity', 'status', 'created_at', 'updated_at']


# class EventMembershipSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#     event = serializers.ReadOnlyField(source='event.name')

#     class Meta:
#         model = EventMembership
#         fields = ['id', 'event', 'user', 'joined_at']


