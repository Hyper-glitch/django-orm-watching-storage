from django.utils.timezone import localtime


def get_duration(visit):
    duration = localtime() - visit.entered_at
    return duration


def format_duration(visit):
    duration = get_duration(visit)
    seconds = duration.total_seconds()
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    return f'{hours} ч {minutes} мин'
