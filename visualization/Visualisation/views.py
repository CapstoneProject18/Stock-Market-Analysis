from django.shortcuts import render

def chart(request):
    return render(request, 'visualisation/chart.html')

# Create your views here.
