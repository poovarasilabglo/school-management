from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsTeacherOrIsStudent(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user.is_student or request.user.is_teacher)
        return False


class IsTeacher(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user.is_staff or request.user.is_teacher)
        return False


class IsTeacherOrIsStudentOrIsParent(IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return bool(request.user.is_student or request.user.is_teacher or request.user.is_parent)
        return False
