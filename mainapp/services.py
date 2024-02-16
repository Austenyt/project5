from django.core.cache import cache

from config import settings


def get_cached_subjects_for_student(student_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list{self.object.pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = self.object.subject_set.all()
            cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()
