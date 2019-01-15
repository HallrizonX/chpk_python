from django.contrib.auth.models import User


class DBAudit:
    """ Class for make audit data in db"""

    # Check if was username
    @staticmethod
    def check_username(username):
        try:
            User.objects.get(username=str(username))
            return False
        except User.DoesNotExist:
            return True

    # Check if was email
    @staticmethod
    def check_email(email):
        try:
            User.objects.get(username=str(email))
            return False
        except User.DoesNotExist:
            return True
