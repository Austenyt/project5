from django.core.management import BaseCommand

from mainapp.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {'last_name': 'Petrov', 'first_name': 'Petr'},
            {'last_name': 'Kozlov', 'first_name': 'Kozel'},
            {'last_name': 'Baranov', 'first_name': 'Baran'},
            {'last_name': 'Orlov', 'first_name': 'Orel'}
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )

        Student.objects.bulk_create(students_for_create)
