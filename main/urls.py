from django.urls import path
from .views import *

urlpatterns = [
# Filter for Employee
    path('filter-employee-by-id/', filter_employee_by_id),
    path('filter-employee/', filter_employee),
# Filter for Student
    path('filter-student/', filter_student),
# Filter for Course
    path('filter-course/', filter_course),
# Filter for Room
    path('filter-room/', filter_room),
# Filter for Homework
    path('filter-homework/', filter_homework)

]