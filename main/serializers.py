from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class DaysSerializers(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = "__all__"


class GroupsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class HomeworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = "__all__"


class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = "__all__"


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"