from django.shortcuts import render

# Create your views here.
def question(request):
    return render(request, 'polls/question.html')

def answer(request):
    return render(request, 'polls/answer.html')

def where(request):
    return render(request, 'polls/where.html')