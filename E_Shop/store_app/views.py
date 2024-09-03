from django.shortcuts import render

# Create your views here.
def BASE(request):
    return render(request, 'Main/base.html')