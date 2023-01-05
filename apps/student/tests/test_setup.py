from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.models import User
from apps.student.models import Student
from apps.teacher.models import Teacher


class TestSetup(APITestCase):
    def setUp(self):
        admin_credentials = {
            "username": "admin",
            "password": "admin"
        }
        student_credentials = {
            "username": "student",
            "password": "password",
            "is_student": True,
        }
        teacher_credentials = {
            "username": "teacher",
            "password": "password",
            "is_teacher": True,
        }
        admin = User.objects.create_superuser(**admin_credentials)
        student = User.objects.create_user(**student_credentials)
        teacher = User.objects.create_user(**teacher_credentials)
        user = User.objects.create(username="student10", email="student1@gmail.com")

        self.teacher_post = Teacher(
            user= teacher,
            teacher_id="TE256",
            name="malar",
            dob="2000-03-03",
            gender="female",
            phone="7733580241",
            address="new",
            join_year="2023"
        )
        self.teacher_post.save()
        
        self.student_post = Student.objects.create(
            user= User.objects.get(id = user.id),
            teacher= Teacher.objects.get(user = self.teacher_post.pk),
            student_id="S246",
            name="mahi",
            dob="1996-04-08",
            gender="male",
            father_name="vino",
            mother_name="kani",
            phone="9536842685",
            address="text",
            std="6",
            session_year="2022",
            roll_number="568",
        )
        self.teacher_post = Teacher(
            user="teacher",
            teacher_id="TE256",
            name="malar",
            dob="1799-09-20",
            gender="female",
            phone="7733580241",
            address="new",
            join_year="2023"
        )
        self.teacher_post.save()

        admin_tokens = RefreshToken.for_user(admin)
        student_tokens = RefreshToken.for_user(student)
        teacher_token = RefreshToken.for_user(teacher)

        self.admin = "Bearer " + str(admin_tokens.access_token)
        self.student = "Bearer " + str(student_tokens.access_token)
        self.teacher = "Bearer " + str(teacher_token.access_token)
    


        return super().setUp()
 