from office.utils.InterfaceOffice import TeacherOffice, StudentOffice


class OfficeFactory:

    @staticmethod
    def create(user)-> object:

        if user.access_profile == 'teacher':
            return TeacherOffice(user)

        if user.access_profile == 'student':
            return StudentOffice(user)

        return False
