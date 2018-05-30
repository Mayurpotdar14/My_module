from django.shortcuts import render
from .models import Person


def index(request):
    all_data = Person.objects.all
    context = {"Database Content: ", all_data}
    return render(request, 'Person/index.html', context)

# Create your views here.
