from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

""" Start Filter User"""
@api_view(['GET'])
def filter_user(request):
    phone_number = request.GET.get('phone_number')
    address = request.GET.get('address')
    birthday = request.GET.get('birthday')
    gender = request.GET.get('gender')
    status = request.GET.get('status')
    balance = request.GET.get('balance')
    filters = {}
    if phone_number is not None:
        filters['phone_number'] = phone_number
    if address is not None:
        filters['address'] = address
    if birthday is not None:
        filters['birthday'] = birthday
    if gender is not None:
        filters['gender'] = gender
    if status is not None:
        filters['status'] = status
    if balance is not None:
        filters['balance'] = balance
    user = User.objects.filter(**filters)
    ser = UserSerializers(user, many=True)
""" Enb Filter User"""

""" Start  Filter Employee """


@api_view(['GET'])
def filter_employee(request):
    id = request.GET.get('id')
    user = request.GET.get('user')
    salary = request.GET.get('salary')
    specialty = request.GET.get('specialty')
    percentage = request.GET.get('percentage')
    number = request.GET.get('number')
    extra_number = request.GET.get('extra_number')
    status = request.GET.get('status')
    filters = {}
    if id is not None:
        filters['id'] = id
    if user is not None:
        filters['user'] = user
    if salary is not None:
        filters['salary'] = salary
    if specialty is not None:
        filters['specialty'] = specialty
    if percentage is not None:
        filters['percentage'] = percentage
    if number is not None:
        filters['number'] = number
    if extra_number is not None:
        filters['extra_number'] = extra_number
    if status is not None:
        filters['status'] = status
    employee = Employee.objects.filter(**filters)
    ser = EmployeeSerializers(employee, many=True)

""" End  Filter Employee """


"""Start Filter Student  """

@api_view(['GET'])
def filter_student(request):
    user = request.GET.get('user')
    number = request.GET.get('number')
    extra_number = request.GET.get('extra_number')
    status = request.GET.get('status')
    filters = {}
    if user is not None:
        filters['user'] = user
    if number is not None:
        filters['number'] = number
    if extra_number is not None:
        filters['extra_number'] = extra_number
    if status is not None:
        filters['status'] = status
    student = Student.objects.filter(**filters)
    ser = StudentSerializers(student, many=True)

"""End Filter Student  """

""" Start Filter Course"""

@api_view(['GET'])
def filter_course(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    duration = request.GET.get('duration')
    price = request.GET.get('price')
    filters = {}
    if id is not None:
        filters['id'] = id
    if name is not None:
        filters['name'] = name
    if duration is not None:
        filters['duration'] = duration
    if price is not None:
        filters['price'] = price
    course = Course.objects.filter(**filters)
    ser = CourseSerializers(course, many=True)

""" End Filter Course"""

""" Start Filter Room"""

@api_view(['GET'])
def filter_room(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    capacity = request.GET.get('capacity')
    filters = {}
    if id is not None:
        filters['id'] = id
    if name is not None:
        filters['name'] = name
    if capacity is not None:
        filters['capacity'] = capacity
    room = -Room.objects.filter(**filters)
    ser = RoomSerializers(room, many=True)

""" End Filter Room"""

""" Start Filter Homework """

@api_view(['GET'])
def filter_homework(request):
    id = request.GET.get('id')
    group = request.GET.get('group')
    filters = {}
    if id is not None:
        filters['id'] = id
    if group is not None:
        filters['group'] = group
    homework = Homework.objects.filter(**filters)
    ser = HomeworkSerializers(homework, many=True)
    return Response(ser.data)

""" End Filter Homework """


"""Start Filter Groups"""

@api_view(['GET'])
def filter_groups(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    course = request.GET.get('course')
    teacher = request.GET.get('teacher')
    students = request.GET.get('students')
    archive_students = request.GET.get('archive_students')
    room = request.GET.get('room')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')
    days = request.GET.get('days')
    start_hour = request.GET.get('start_hour')
    end_hour = request.GET.get('end_hour')
    info = request.GET.get('info')
    status = request.GET.get('status')
    created_at = request.GET.get('created_at')
    filters = {}
    if id is not None:
        filters['id'] = id
    if name is not None:
        filters['name'] = name
    if course is not None:
        filters['course'] = course
    if teacher is not None:
        filters['teacher'] = teacher
    if students is not None:
        filters['students'] = students
    if archive_students is not None:
        filters['archive_students'] = archive_students
    if room is not None:
        filters['room'] = room
    if start_time is not None:
        filters['start_time'] = start_time
    if end_time is not None:
        filters['end_time'] = end_time
    if days is not None:
        filters['days'] = days
    if start_hour is not None:
        filters['start_hour'] = start_hour
    if end_hour is not None:
        filters['end_hour'] = end_hour
    if info is not None:
        filters['info'] = info
    if status is not None:
        filters['status'] = status
    if created_at is not None:
        filters['created_at'] = created_at
    group = -Groups.objects.filter(**filters)
    ser = GroupsSerializers(group, many=True)
    return Response(ser.data)

"""End Filter Group"""

"""Start Filter Payment"""
@api_view(['GET'])
def filter_payment(request):
    id = request.GET.get('id')
    user = request.GET.get('user')
    amount = request.GET.get('amount')
    payment_date = request.GET.get('payment_date')
    filters = {}
    if id is not None:
        filters['id'] = id
    if user is not None:
        filters['user'] = user
    if amount is not None:
        filters['amount'] = amount
    if payment_date is not None:
        filters['payment_date'] = payment_date
    payment = -Payment.objects.filter(**filters)
    ser = PaymentSerializers(payment, many=True)
    return Response(ser.data)

"""End Filter Payment"""

"""Start Filter """

@api_view(['GET'])
def filter_attendance(request):
    user = request.GET.get('user')
    date = request.GET.get('date')
    is_present = request.GET.get('is_present')
    filters = {}
    if user is not None:
        filters['user'] = user
    if date is not None:
        filters['date'] = date
    if is_present is not None:
        filters['is_present'] = is_present
    attendance = -Attendance.objects.filter(**filters)
    ser = AttendanceSerializers(attendance, many=True)
    return Response(ser.data)

"""End filter Attendance"""

"""Start filter Exam"""

@api_view(['GET'])
def filter_exam(request):
    group = request.GET.get('group')
    exam_teacher = request.GET.get('exam_teacher')
    min_score = request.GET.get('min_score')
    max_score = request.GET.get('max_score')
    room = request.GET.get('room')
    date = request.GET.get('date')
    filters = {}
    if group is not None:
        filters['group'] = group
    if exam_teacher is not None:
        filters['exam_teacher'] = exam_teacher
    if min_score is not None:
        filters['min_score'] = min_score
    if max_score is not None:
        filters['max_score'] = max_score
    if room is not None:
        filters['room'] = room
    if date is not None:
        filters['date'] = date

    exam = -Exam.objects.filter(**filters)
    ser = ExamSerializers(exam, many=True)
    return Response(ser.data)

"""End filter Exam"""

"""Start filter Notification"""

@api_view(['GET'])
def filter_notification(request):
    student = request.GET.get('student')
    created_at = request.GET.get('created_at')
    filters = {}
    if student is not None:
        filters['student'] = student
    if created_at is not None:
        filters['created_at'] = created_at

    notification = -Notification.objects.filter(**filters)
    ser = NotificationSerializers(notification, many=True)
    return Response(ser.data)


"""End filter Notification"""