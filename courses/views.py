from .models import Course
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
)
from .serializers import CoursesSerizalizer, CoursePatchSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuperUser, IsOwnerAccount


class CourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_url_kwarg = "course_id"
    queryset = Course.objects.all()
    serializer_class = CoursesSerizalizer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        return Course.objects.filter(students=self.request.user)


class CourseDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerAccount]
    lookup_url_kwarg = "course_id"
    queryset = Course.objects.all()
    serializer_class = CoursesSerizalizer


class CoursePatch(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_url_kwarg = "course_id"
    queryset = Course.objects.all()
    serializer_class = CoursePatchSerializer
