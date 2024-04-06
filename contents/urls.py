from django.urls import path
from contents.views import ContentView, ContentDetailView

urlpatterns = [
    path("courses/<course_id>/contents/", ContentView.as_view()),
    path("courses/<course_id>/contents/<content_id>/", ContentDetailView.as_view()),
]
