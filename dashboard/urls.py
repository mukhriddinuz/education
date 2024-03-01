from django.urls import path
from .views import *

urlpatterns = [
    # CRUD for Employee
    path('employees/', GetEmployee.as_view(), name='get_employee'),
    path('employees/create/', CreateEmployee.as_view(), name='create_employee'),
    path('employees/update/<int:pk>/', UpdateEmployee.as_view(), name='update_employee'),
    path('employees/delete/<int:pk>/', DeleteEmployee.as_view(), name='delete_employee'),

    # CRUD for Student
    path('students/', GetStudent.as_view(), name='get_student'),
    path('students/create/', CreateStudent.as_view(), name='create_student'),
    path('students/update/<int:pk>/', UpdateStudent.as_view(), name='update_student'),
    path('students/delete/<int:pk>/', DeleteStudent.as_view(), name='delete_student'),

    # CRUD for Course
    path('courses/', GetCourse.as_view(), name='get_course'),
    path('courses/create/', CreateCourse.as_view(), name='create_course'),
    path('courses/update/<int:pk>/', UpdateCourse.as_view(), name='update_course'),
    path('courses/delete/<int:pk>/', DeleteCourse.as_view(), name='delete_course'),

    # CRUD for Room
    path('rooms/', GetRoom.as_view(), name='get_room'),
    path('rooms/create/', CreateRoom.as_view(), name='create_room'),
    path('rooms/update/<int:pk>/', UpdateRoom.as_view(), name='update_room'),
    path('rooms/delete/<int:pk>/', DeleteRoom.as_view(), name='delete_room'),

    # CRUD for Days
    path('days/', GetDays.as_view(), name='get_days'),
    path('days/create/', CreateDays.as_view(), name='create_days'),
    path('days/update/<int:pk>/', UpdateDays.as_view(), name='update_days'),
    path('days/delete/<int:pk>/', DeleteDays.as_view(), name='delete_days'),

    # CRUD for Groups
    path('groups/', GetGroups.as_view(), name='get_groups'),
    path('groups/create/', CreateGroups.as_view(), name='create_groups'),
    path('groups/update/<int:pk>/', UpdateGroups.as_view(), name='update_groups'),
    path('groups/delete/<int:pk>/', DeleteGroups.as_view(), name='delete_groups'),

    # CRUD for Payment
    path('payments/', GetPayment.as_view(), name='get_payment'),
    path('payments/create/', CreatePayment.as_view(), name='create_payment'),
    path('payments/update/<int:pk>/', UpdatePayment.as_view(), name='update_payment'),
    path('payments/delete/<int:pk>/', DeletePayment.as_view(), name='delete_payment'),

    # CRUD for Attendance
    path('attendances/', GetAttendance.as_view(), name='get_attendance'),
    path('attendances/create/', CreateAttendance.as_view(), name='create_attendance'),
    path('attendances/update/<int:pk>/', UpdateAttendance.as_view(), name='update_attendance'),
    path('attendances/delete/<int:pk>/', DeleteAttendance.as_view(), name='delete_attendance'),

    # CRUD for Homework
    path('homeworks/', GetHomework.as_view(), name='get_homework'),
    path('homeworks/create/', CreateHomework.as_view(), name='create_homework'),
    path('homeworks/update/<int:pk>/', UpdateHomework.as_view(), name='update_homework'),
    path('homeworks/delete/<int:pk>/', DeleteHomework.as_view(), name='delete_homework'),

    # CRUD for Exam
    path('exams/', GetExam.as_view(), name='get_exam'),
    path('exams/create/', CreateExam.as_view(), name='create_exam'),
    path('exams/update/<int:pk>/', UpdateExam.as_view(), name='update_exam'),
    path('exams/delete/<int:pk>/', DeleteExam.as_view(), name='delete_exam'),

    # CRUD for Notification
    path('notifications/', GetNotification.as_view(), name='get_notification'),
    path('notifications/create/', CreateNotification.as_view(), name='create_notification'),
    path('notifications/update/<int:pk>/', UpdateNotification.as_view(), name='update_notification'),
    path('notifications/delete/<int:pk>/', DeleteNotification.as_view(), name='delete_notification'),
]

