from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    detailed_visits = []

    for visit in visits:
        detailed_visit = {
            'entered_at': visit.entered_at,
            'duration': visit.get_duration(),
            'is_strange': visit.is_long(),
        }
        detailed_visits.append(detailed_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': detailed_visits
    }
    return render(request, 'passcard_info.html', context)
