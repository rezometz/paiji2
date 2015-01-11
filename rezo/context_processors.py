from django.conf import settings

def get_admin_email(request):
    return {
        'admin_email': settings.ADMIN_EMAIL,
    }