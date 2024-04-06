
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import View, Request
from contents.models import Content
from courses.models import Course


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_superuser


class IsOwnerAccount(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        course = Course.objects.get(pk=view.kwargs["course_id"])
        return request.method in SAFE_METHODS and len(course.students.filter(id=request.user.id)) >= 1