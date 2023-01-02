from django.db import models
from apps.user.models import User


GENDER_CHOICES = (('Male', 'male'),
                  ('Female', 'female'))  


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add= True)
     updated_on = models.DateTimeField(auto_now= True)
     class Meta:
         abstract = True


class Teacher(TimeStampedModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    teacher_id = models.CharField(max_length= 30,unique= True)
    name = models.CharField(max_length= 30)
    image = models.ImageField(upload_to= "images/")
    dob = models.DateField()
    gender = models.CharField(max_length= 10,choices= GENDER_CHOICES)
    phone = models.CharField(max_length= 15)
    address = models.CharField(max_length= 50)
    join_year = models.IntegerField()

    def __str__(self):
        return self.user.username