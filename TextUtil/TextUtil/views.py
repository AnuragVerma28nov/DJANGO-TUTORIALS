# i have created this file - Anurag
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>AnuragVerma<h1>") 
def about(request):
    return HttpResponse("This is About Page")
def contact(request):
    return HttpResponse("This is contact Page")
def github(request):
    return HttpResponse('''Click On Link<br> <a href="https://github.com/AnuragVerma28nov"> Anurag Link </a>''')