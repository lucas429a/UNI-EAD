from django.urls import path
from courses.views import CourseView, CourseDetailView, CoursePatch

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<course_id>/", CourseDetailView.as_view()),
    path("courses/<course_id>/students/", CoursePatch.as_view()),
]
