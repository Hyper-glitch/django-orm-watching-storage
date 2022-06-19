from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    who_in_storage = []

    for visit in not_leaved_visits:
        duration = visit.get_duration()
        non_closed_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(duration=duration),
        }
        who_in_storage.append(non_closed_visit)

    context = {
        'non_closed_visits': who_in_storage,
    }
    return render(request, 'storage_information.html', context)
