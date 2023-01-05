from django.db import models
from django.contrib.auth.models import AbstractUser

'''send_mail reset_password'''
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 


class User(AbstractUser):
    is_accountant = models.BooleanField(default = False)
    is_teacher = models.BooleanField(default = False)
    is_student = models.BooleanField(default = False)
    is_parent = models.BooleanField(default = False)

    def __str__(self):
        return self.username


'''class Accountant(models.Model):
    user =  models.OneToOneField(User, on_delete = models.CASCADE)
    emp_id = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.user.username'''
    

 #                '''set_password'''

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "Don't Reply <labglo@gmail.com> ",
        # to:
        [reset_password_token.user.email]
    )
    
