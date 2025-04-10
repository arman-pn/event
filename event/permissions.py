from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # روش‌های فقط خواندنی (GET, HEAD, OPTIONS) همیشه مجازن
        if request.method in permissions.SAFE_METHODS:
            return True

        # فقط اگه یوزر، creator اون event باشه اجازه داره ویرایش کنه
        return obj.creator == request.user
