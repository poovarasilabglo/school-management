from student.tests.test_setup import TestSetup
from django.urls import reverse
from rest_framework import status
import json


class StudentTests(TestSetup):

    list_url = reverse("student-list")

    def test_student_can_get(self):

        response = self.client.get(self.list_url, HTTP_AUTHORIZATION=self.student)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_teacher_can_get(self):

    #     response = self.client.get(self.list_url, HTTP_AUTHORIZATION=self.teacher)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # def test_teacher_can_post(self):

    #     self.student = {
    #         "user": {
    #             "username": "test1",
    #             "first_name": "e",
    #             "last_name": "e",
    #             "email": "raja@gmail.com",
    #             "password": "pass",
    #             "is_student": "true",
    #         },
    #         "name": "test",
    #         "student_id":"SH564",
    #         "dob":"19-07-1996",
    #         "gender":"male",
    #         "father_name":"mani",
    #         "mother_name":"kani",
    #         "phone":"7586952473",
    #         "address":"text1",
    #         "std":"7",
    #         "session_year":"2022",
    #         "roll_number":"68",

            
    #     }

    #     response = self.client.post(
    #         reverse("student-list"),
    #         self.student,
    #         HTTP_AUTHORIZATION=self.teacher,
    #         format="json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_student_cannot_post(self):

    #     response = self.client.post(
    #         self.list_url,
    #         data=self.valid_post,
    #         HTTP_AUTHORIZATION=self.student,
    #         format="json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # def test_student_can_partial_update_put(self):
    #     response = self.client.patch(
    #         reverse("student-detail", kwargs={"pk": self.student_post.pk}),
    #         {    
    #             "name":"new",
    #             "father_name":"fa",
    #             "mother_name":"mo",
    #             "dob": "20-05-2000",
    #             "gender": "male",
    #             "address": "text",
    #             "mobile": "7538596482",
    #         },
    #         HTTP_AUTHORIZATION=self.student,
    #         format="json",
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

