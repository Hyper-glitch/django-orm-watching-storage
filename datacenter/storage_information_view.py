from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    serialized_visits = []

    for visit in not_leaved_visits:
        duration = visit.get_duration()
        serialized_visit = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(duration=duration),
        }
        serialized_visits.append(serialized_visit)

    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
