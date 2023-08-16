from django.shortcuts import render

# Create your views here.
def answer(request):
    return render(request, 'answer.html')