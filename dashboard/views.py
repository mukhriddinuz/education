from django.shortcuts import render
from rest_framework.response import Response
from datetime import datetime, timedelta
import datetime
from dateutil.relativedelta import relativedelta
from rest_framework.decorators import api_view
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
# class CreateGroups(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = GroupsSerializers


@api_view(['POST'])
def CreateGroup(request):
    name = request.POST.get('name')
    course = request.POST.get('course')
    teacher = request.POST.get('teacher')
    students = request.POST.getlist('students')
    archive_students = request.POST.getlist('archive_students')
    room = request.POST.get('room')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    days = request.POST.getlist('days')
    start_hour = request.POST.get('start_hour')
    end_hour = request.POST.get('end_hour')
    info = request.POST.get('info')
    status = request.POST.get('status')

    try:
        course_id = int(course)
        teacher_id = int(teacher)
        room_id = int(room)
        status = int(status)
    except ValueError:
        raise ValidationError("Invalid integer value for course, teacher, room, or status")

    is_blank = Groups.objects.filter(room_id=room_id, start_hour__lte=start_hour, end_hour__gte=end_hour, days__in=days)
    if is_blank.exists():
        error_message = 'Bu xonada dars mavjud!\n'
        for item in is_blank:
            error_message += f'{item}\n'
        raise ValidationError(error_message)
    else:
        group = Groups.objects.create(
            name=name,
            course_id=course_id,
            teacher_id=teacher_id,
            room_id=room_id,
            start_time=start_time,
            end_time=end_time,
            start_hour=start_hour,
            end_hour=end_hour,
            info=info,
            status=status,
        )
        group.students.add(*students)
        group.archive_students.add(*archive_students)
        group.days.add(*days)

        ser = GroupsSerializers(group)
        return Response(ser.data)


# class UpdateGroups(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = GroupsSerializers


@api_view(['PUT'])
def UpdateGroup(request, pk):
    name = request.POST.get('name')
    course = request.POST.get('course')
    teacher = request.POST.get('teacher')
    students = request.POST.getlist('students')
    archive_students = request.POST.getlist('archive_students')
    room = request.POST.get('room')
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    days = request.POST.getlist('days')
    start_hour = request.POST.get('start_hour')
    end_hour = request.POST.get('end_hour')
    info = request.POST.get('info')
    status = request.POST.get('status')

    try:
        course_id = int(course)
        teacher_id = int(teacher)
        room_id = int(room)
        status = int(status)
    except ValueError:
        raise ValidationError("Invalid integer value for course, teacher, room, or status")

    is_blank = Groups.objects.filter(room_id=room_id, start_hour__lte=start_hour, end_hour__gte=end_hour, days__in=days)
    if is_blank.exists() and all(i.id != pk for i in is_blank):
        error_message = 'Bu xonada dars mavjud!\n'
        for item in is_blank:
            error_message += f'{item}\n'
        raise ValidationError(error_message)
    else:
        group = Groups.objects.get(pk=pk)
        group.name = name if name else group.name
        group.course_id = course_id if course_id else group.course_id
        group.teacher_id = teacher_id if teacher_id else group.teacher_id
        group.room_id = room_id if room_id else group.room_id
        group.start_time = start_time if start_time else group.start_time
        group.end_time = end_time if end_time else group.end_time
        group.start_hour = start_hour if start_hour else group.start_hour
        group.end_hour = end_hour if end_hour else group.end_hour
        group.info = info if info else group.info
        group.status = status if status else group.status

        group.save()

        group.students.add(*students)
        group.archive_students.add(*archive_students)
        group.days.add(*days)

        ser = GroupsSerializers(group)
        return Response(ser.data)


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
