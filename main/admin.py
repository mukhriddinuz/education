from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


@admin.register(User)
class EmployeeAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('phone_number', "extra_phone_number", "address", "birthday", "gender", "status", "balance", )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Room)
admin.site.register(Days)
admin.site.register(Groups)
admin.site.register(Payment)
admin.site.register(Attendance)
admin.site.register(Homework)
admin.site.register(Exam)
admin.site.register(Notification)
