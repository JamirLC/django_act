from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def question(request):
    return render(request, 'question.html')

def answer(request):
    return render(request, 'answer.html')

def where(request):
    return render(request, 'where.html')