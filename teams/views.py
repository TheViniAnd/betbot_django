from django.shortcuts import render
from django.utils import timezone
from .models import Time_Kill, Totals, Team

def totals(request):
    posts = Time_Kill.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    times = Time_Kill.objects.filter(team__name='Virtus.Pro').first()
    t2 = Time_Kill.objects.filter(team__name="Virtus.pro")
    print(t2)
    it = []
    print(times)
    #for tem in times:
    #    it.append(tem)
    #print(it)
    return render(request, 'teams/totals.html', {'posts': posts})