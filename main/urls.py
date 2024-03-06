from django.urls import path
from .views import *

urlpatterns = [
    path('filter-employee/', filter_employee),
    path('filter-student/', filter_student),
    path('filter-course/', filter_course),
    path('filter-room/', filter_room),
    path('filter-homework/', filter_homework),

    path('filter-groups/', filter_groups),
    path('filter-payment/', filter_payment),
    path('filter-attendance/', filter_attendance),
    path('filter-exam/', filter_exam),
    path('filter-notification/', filter_notification),

]