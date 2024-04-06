from rest_framework import serializers
from .models import Course
from accounts.models import Account
from contents.serializers import ContentSerizalizer
from students_courses.serializers import StudentCourseSerizalizer


class CoursesSerizalizer(serializers.ModelSerializer):
    contents = ContentSerizalizer(read_only=True, many=True)
    students_courses = StudentCourseSerizalizer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]


class CoursePatchSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerizalizer(many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses"
        ]
        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance: Course, validated_data: dict):
        students = []
        students_not_found = []

        for student in validated_data["students_courses"]:
            found_student = Account.objects.filter(email=student["student"]["email"]).first()
            if not found_student:
                students_not_found.append(student["student"]["email"])
            else:
                students.append(found_student)
        if students_not_found:
            raise serializers.ValidationError({
                    "detail": f"No active accounts was found: {', '.join(students_not_found)}."
                })
        if not self.partial:
            instance.students.add(*students)
            return instance
