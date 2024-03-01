from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.serializers import *
from main.models import *


""" Start Crud Model """


#<<<<<<<<<<<<<<< Start Crud Employee>>>>>>>>>>>>>>>>>
class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class DeleteEmployee(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

#<<<<<<<<<<<<<< End Crud Employee>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Student>>>>>>>>>>>>>>>>>
class GetStudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
class CreateStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class UpdateStudent(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class DeleteStudent(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

#<<<<<<<<<<<<<< End Crud Student>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Course>>>>>>>>>>>>>>>>>
class GetCourse(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
class CreateCourse(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class UpdateCourse(UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class DeleteCourse(DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

#<<<<<<<<<<<<<< End Crud Course>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Room>>>>>>>>>>>>>>>>>
class GetRoom(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
class CreateRoom(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class UpdateRoom(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

class DeleteRoom(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers

#<<<<<<<<<<<<<< End Crud Room>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Days>>>>>>>>>>>>>>>>>
class GetDays(ListAPIView):
    queryset = Days.objects.all()
    serializer_class = DaysSerializers
class CreateDays(ListCreateAPIView):
    queryset = Days.objects.all()
    serializer_class = DaysSerializers

class UpdateDays(UpdateAPIView):
    queryset = Days.objects.all()
    serializer_class = DaysSerializers

class DeleteDays(DestroyAPIView):
    queryset = Days.objects.all()
    serializer_class = DaysSerializers

#<<<<<<<<<<<<<< End Crud Days>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Groups>>>>>>>>>>>>>>>>>
class GetGroups(ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializers
class CreateGroups(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = GroupsSerializers

class UpdateGroups(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = GroupsSerializers

class DeleteGroups(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = GroupsSerializers

#<<<<<<<<<<<<<< End Crud Groups>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Payment>>>>>>>>>>>>>>>>>
class GetPayment(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers
class CreatePayment(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class UpdatePayment(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class DeletePayment(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

#<<<<<<<<<<<<<< End Crud Payment>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Attendance>>>>>>>>>>>>>>>>>
class GetAttendance(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers
class CreateAttendance(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers

class UpdateAttendance(UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers

class DeleteAttendance(DestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializers

#<<<<<<<<<<<<<< End Crud Attendance>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Homework>>>>>>>>>>>>>>>>>
class GetHomework(ListAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers
class CreateHomework(ListCreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers

class UpdateHomework(UpdateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers

class DeleteHomework(DestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializers

#<<<<<<<<<<<<<< End Crud Homework>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Exam>>>>>>>>>>>>>>>>>
class GetExam(ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers
class CreateExam(ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers

class UpdateExam(UpdateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers

class DeleteExam(DestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers

#<<<<<<<<<<<<<< End Crud Exam>>>>>>>>>>>>>>>>>

#<<<<<<<<<<<<<<< Start Crud Notification>>>>>>>>>>>>>>>>>
class GetNotification(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers
class CreateNotification(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

class UpdateNotification(UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

class DeleteNotification(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers

#<<<<<<<<<<<<<< End Crud Notification>>>>>>>>>>>>>>>>>







"""" End Crud Model """
