from django.shortcuts import render

# Create your views here.
def home(request):
    tamplate_name = 'home.html'
    context = {
        'title': 'OSBA',
        'saudacao': 'Olá OSBA!'
    }
    return render(request, tamplate_name, context)