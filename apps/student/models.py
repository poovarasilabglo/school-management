from django.db import models
from apps.user.models import User
from apps.teacher.models import Teacher


GENDER_CHOICES = (('Male', 'male'),
                  ('Female', 'female'))  


APPROVED = 1
PENDING = 2
CANCEL = 3
LEAVEREQUEST_CHOICES = (('APPROVED','Approved'),
                        ('PENDING','Pending'),
                        ('CANCEL','Cancel'))


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add= True)
     updated_on = models.DateTimeField(auto_now= True)
     class Meta:
         abstract = True


class Student(TimeStampedModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    student_id = models.CharField(max_length= 30, unique= True)
    name = models.CharField(max_length= 30)
    profile_picture = models.ImageField(upload_to= "images/")
    dob =  models.DateField()
    gender = models.CharField(max_length= 10, choices= GENDER_CHOICES)
    father_name = models.CharField(max_length= 20)
    mother_name = models.CharField(max_length= 20)
    phone = models.CharField(max_length= 15)
    address = models.CharField(max_length= 50)
    std = models.CharField(max_length= 15)
    session_year = models.CharField(max_length= 30)
    roll_number = models.PositiveIntegerField()
    
    def __str__(self):
        return self.user.username


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    subject_code = models.CharField(max_length= 15,unique= True)
    subject_name = models.CharField(max_length= 30)
    subject_mark = models.IntegerField()


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    absent = models.BooleanField(default=False)
    half = models.BooleanField(default=False)


class LeaveRequest(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE)
    request = models.BooleanField(default= False)
    status = models.IntegerField(choices= LEAVEREQUEST_CHOICES, default= 'Pending')
    remark = models.TextField()


