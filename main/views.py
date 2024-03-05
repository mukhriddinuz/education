from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

""" Start  Filter Employee """

@api_view(['GET'])
def filter_employee_by_id(request):
    id = request.GET.get('id')
    employee = Employee.objects.filter(id=id)
    ser = EmployeeSerializers(employee, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_employee(request):
    salary = request.GET.get('salary')
    specialty = request.GET.get('specialty')
    percentage = request.GET.get('percentage')
    number = request.GET.get('number')
    extra_number = request.GET.get('extra_number')
    status = request.GET.get('status')
    filters = {}
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

    # Shartlar bo'yicha filtr qilamiz
    employee = Employee.objects.filter(**filters)
    ser = EmployeeSerializers(employee, many=True)

""" End  Filter Employee """


"""Start Filter Student  """

@api_view(['GET'])
def filter_student(request):
    number = request.GET.get('number')
    extra_number = request.GET.get('extra_number')
    status = request.GET.get('status')
    filters = {}
    if number is not None:
        filters['number'] = number
    if extra_number is not None:
        filters['extra_number'] = extra_number
    if status is not None:
        filters['status'] = status

    # Shartlar bo'yicha filtr qilamiz
    student = Student.objects.filter(**filters)
    ser = StudentSerializers(student, many=True)

"""End Filter Student  """

""" Start Filter Course"""
@api_view(['GET'])
def filter_course(request):
    name = request.GET.get('name')
    duration = request.GET.get('duration')
    price = request.GET.get('price')
    filters = {}
    if name is not None:
        filters['name'] = name
    if duration is not None:
        filters['duration'] = duration
    if price is not None:
        filters['price'] = price

    # Shartlar bo'yicha filtr qilamiz
    course = Course.objects.filter(**filters)
    ser = CourseSerializers(course, many=True)

""" End Filter Course"""

""" Start Filter Room"""
@api_view(['GET'])
def filter_room(request):
    name = request.GET.get('name')
    capacity = request.GET.get('capacity')
    filters = {}
    if name is not None:
        filters['name'] = name
    if capacity is not None:
        filters['capacity'] = capacity
    # Shartlar bo'yicha filtr qilamiz
    room = -Room.objects.filter(**filters)
    ser = RoomSerializers(room, many=True)
""" End Filter Room"""

""" Start Filter Homework """

@api_view(['GET'])
def filter_homework(request):
    group = request.GET.get('group')
    homework = Homework.objects.filter(group=group)
    ser = HomeworkSerializers(homework, many=True)
    return Response(ser.data)

""" End Filter Homework """