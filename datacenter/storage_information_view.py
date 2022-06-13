from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.storage_info_tools import format_duration


def storage_information_view(request):
    passcards = Passcard.objects.all()
    non_closed_visits = []

    for passcard in passcards:
        visits = Visit.objects.filter(passcard=passcard)
        for visit in visits:
            if not visit.leaved_at:
                entered_at = visit.entered_at

                non_closed_visit = {
                    'who_entered': visit.passcard.owner_name,
                    'entered_at': entered_at,
                    'duration': format_duration(entered_at),
                }
                non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
