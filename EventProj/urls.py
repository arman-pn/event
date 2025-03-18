from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.views import EventViewSet, EventLogViewSet, EventMembershipView, EventMembersView



router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event_logs', EventLogViewSet)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/events/<int:event_id>/join/', EventMembershipView.as_view(), name='join_event'),
    path('api/events/<int:event_id>/members/', EventMembersView.as_view(), name='event_members'),
]


