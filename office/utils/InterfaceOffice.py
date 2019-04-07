#from abc import ABC, abstractmethod
from office.models import Teacher


class Office:
    template: str = ""

    def __init__(self, user: object):
        self.office = user


class StudentOffice(Office):
    """ Class for student office"""
    template: str = 'office/student/index.html'

    def get_context(self) -> dict:
        return {
            "user": self.office,
        }


class TeacherOffice(Office):
    """Class for teacher office"""
    template: str = 'office/teacher/index.html'

    def get_context(self) -> dict:
        teacher = Teacher.objects.get(profile__user=self.office.user)
        return {
            "user": self.office,
            "subjects": teacher.subjects,
            "files": teacher.files.all().order_by('subject__group__number', 'subject__name')
        }
