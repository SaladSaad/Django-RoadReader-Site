from django.shortcuts import render


def map(request):
    return render(request, 'map.html', {'title': 'Map'})


def extra(request):
    return render(request, 'extra.html', {'title': 'Extra'})
