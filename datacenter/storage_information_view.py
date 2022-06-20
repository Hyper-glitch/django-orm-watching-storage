from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit


def storage_information_view(request):
    passcards = Passcard.objects.all()
    serialized_visits = []

    for passcard in passcards:
        visits = Visit.objects.filter(passcard=passcard)
        for visit in visits:
            if not visit.leaved_at:
                serialized_visit = {
                    'who_entered': visit.passcard.owner_name,
                    'entered_at': visit.entered_at,
                    'duration': visit.format_duration(),
                }
                serialized_visits.append(serialized_visit)

    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
