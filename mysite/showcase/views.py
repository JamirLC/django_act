from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request, 'showcase/show.html')

def sure(request):
    return render(request, 'showcase/sure.html')

def ans(request):
    return render(request, 'showcase/ans.html')
