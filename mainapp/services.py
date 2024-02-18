from django.core.cache import cache

from config import settings
from mainapp.models import Subject


def get_cached_subjects_for_student(student_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list{student_pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Subject.objects.filter(student_pk=student_pk)
            cache.set(key, subject_list)
    else:
        subject_list = Subject.objects.filter(student_pk=student_pk)

    return subject_list
