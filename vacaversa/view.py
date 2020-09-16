
from django.shortcuts import render

def home(request):
    return render(request, 'home1.html')


def reverse(request):
    username = request.GET['username']
    countWords = len(username.split())
    reversedText = username[::-1]

    return render(request, 'reverse.html', {'username':username, 'reversedText':reversedText, 'countWords':countWords})