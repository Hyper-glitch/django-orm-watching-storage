from django.shortcuts import render

from datacenter.models import Passcard


def active_passcards_view(request):
    all_passcards = Passcard.objects.all()
    active_passcards = all_passcards.filter(is_active=True)
    context = {'active_passcards': active_passcards}
    return render(request, 'active_passcards.html', context)
