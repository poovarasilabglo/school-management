'''from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    role = get_role(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_type': str(role),
    }


def get_role(user):
    if user.is_staff:
        return "admin"
    elif user.is_student:
        return "student"
    elif user.is_teacher:
        return "teacher"
    elif user.is_accountant:
        return "accountant"
    elif user.is_parent:
        return "parent"'''
