from django.shortcuts import render


# Create your views here.
def checkers(request):
    return render(request, 'checkers.html')

