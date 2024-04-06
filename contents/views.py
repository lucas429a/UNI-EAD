from .models import Content
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import ContentSerizalizer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsSuperUser, IsOwnerAccount
from django.shortcuts import get_object_or_404
from courses.models import Course
from rest_framework.exceptions import NotFound


class ContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUser]
    lookup_url_kwarg = "course_id"
    queryset = Content.objects.all()
    serializer_class = ContentSerizalizer

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs.get("course_id"))
        serializer.save(course=course)

    def get_queryset(self):
        return Content.objects.filter(course_id=self.kwargs.get("course_id"))


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerAccount]
    queryset = Content.objects.all()
    serializer_class = ContentSerizalizer
    lookup_url_kwarg = "content_id"

    def get_object(self):
        content = Content.objects.filter(pk=self.kwargs.get("content_id")).first()
        if not content:
            raise NotFound("content not found.")
        course = Course.objects.filter(pk=self.kwargs.get("course_id")).first()
        if not course:
            raise NotFound("course not found.")
        self.check_object_permissions(self.request, content)
        return content
