from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import EventView, EventLogView, EventMembershipView, EventMembersView





urlpatterns = [
    path('api/events_log/', EventLogView.as_view(), name='event_list_create'),
    path('api/events_log/<int:event_id>/', EventLogView.as_view(), name='event_detail'),
    path('api/events/', EventView.as_view(), name='event_list_create'),
    path('api/events/<int:event_id>/', EventView.as_view(), name='event_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/events/<int:event_id>/join/', EventMembershipView.as_view(), name='join_event'),
    path('api/events/<int:event_id>/exit/', EventMembersView.as_view(), name='exit_event'),
    path('api/events/<int:event_id>/members/', EventMembersView.as_view(), name='event_members'),
]
