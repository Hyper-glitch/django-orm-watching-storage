from django.shortcuts import render

from datacenter.models import Passcard
from datacenter.models import Visit


def storage_information_view(request):
    passcards = Passcard.objects.all()
    non_closed_visits = []

    for passcard in passcards:
        visits = Visit.objects.filter(passcard=passcard)
        for visit in visits:
            if not visit.leaved_at:
                non_closed_visit = {
                    'who_entered': visit.passcard.owner_name,
                    'entered_at': visit.entered_at,
                    'duration': visit.format_duration(),
                }
                non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
