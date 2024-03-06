from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
import datetime
from dateutil.relativedelta import relativedelta



class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    extra_phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    address = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    GENDER = (
        (0, "Male"),
        (1, "Famale"),
    )
    gender = models.IntegerField(default=0, choices=GENDER)
    STATUS = (
        (0, "Student"),
        (1, "Teacher"),
        (1, "Director"),
        (1, "Admin"),
        (1, "Manager"),
    )
    status = models.IntegerField(default=0, choices=STATUS)
    balance = models.BigIntegerField(default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Employee(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bio = models.TextField()
    specialty = models.CharField(max_length=255)
    experience = models.CharField(max_length=150)
    percentage = models.IntegerField(default=0)

    def clean(self):
        if self.percentage <= 0 or self.percentage >= 100:
            raise ValidationError("0 va 100 oralig'ida bo'lishi shart!")

    def save(self, *args, **kwargs):
        salary = 0
        groups = Groups.objects.filter(teacher_id=self.id)
        for group in groups:
            salary += group.course.price * group.students.count()
        self.salary = (self.percentage / 100) * salary
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.first_name


class Student(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    parent_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    extra_parent_number = models.CharField(max_length=13, unique=True, null=True, blank=True, validators=[
        RegexValidator(
            regex=r'^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='Invalid number'
        )
    ])
    telegram = models.CharField(max_length=50, null=True, blank=True)
    STATUS = (
        (0, "active"),
        (1, "passive"),
        (2, "waiting"),
    )
    status = models.IntegerField(default=0, choices=STATUS)

    def __str__(self):
        return self.user.first_name


class Course(models.Model):
    name = models.CharField(max_length=155)
    duration = models.IntegerField(default=0) #kurs davomiyligi oy hisobida
    price = models.IntegerField(default=0)
    info = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=150)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Days(models.Model):
    day_name = models.CharField(max_length=50)

    def __str__(self):
        return self.day_name


class Groups(models.Model):
    STATUS = (
        (0, "spare"),
        (1, "active"),
        (2, "archive"),
    )
    name = models.CharField(max_length=150, null=True, blank=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Employee, on_delete=models.PROTECT)
    students = models.ManyToManyField(to=User, related_name='groups_students')
    archive_students = models.ManyToManyField(to=User, related_name='groups_archive_students')
    room = models.ForeignKey(to=Room, on_delete=models.PROTECT)
    start_time = models.DateField() #kurs boshlanish sanasi
    end_time = models.DateField(null=True, blank=True) #kurs tugash sanasi
    days = models.ManyToManyField(to=Days)
    start_hour = models.TimeField() # dars boshlanish vaqti
    end_hour = models.TimeField() # dars tugash vaqti
    info = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.name is None:
            self.name = f"{self.start_time} - guruh"
        teacher = self.teacher
        teacher.save()
        super().save(*args, **kwargs)





class Payment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    payment_date = models.DateField(null=True, blank=True)


class Attendance(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)


class Homework(models.Model):
    group = models.ForeignKey(to=Groups, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Employee, on_delete=models.CASCADE, null=True, blank=True)
    work = models.TextField()
    create_at = models.DateTimeField(auto_now=True)


class Exam(models.Model):
    group = models.ForeignKey(to=Groups, on_delete=models.CASCADE)
    exam_teacher = models.ManyToManyField(to=Employee)
    min_score = models.IntegerField(default=30)
    max_score = models.IntegerField(default=100)
    date = models.DateField()
    room = models.ForeignKey(to=Room, on_delete=models.SET_NULL, null=True,)


class Notification(models.Model):
    creator = models.ForeignKey(to=Employee, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(to=User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)



