from django.shortcuts import render
from django.http import HttpResponse
from.models import chd
def index(request):
    mpm=chd.objects.all()
    return render(request,'index.html',{'mpm':mpm})
    #return HttpResponse("<h1><center> WELCOME TO 'MEHFIL'</center></h1">)
def seena(request):
    return HttpResponse("<h1><center> Dr. SAKEENA </center></h1>")
def nachu(request):
    return HttpResponse("<h1><center> Mrs NAZNEEN NISAR </center></h1>")
def ayru(request):
    return HttpResponse("<h1><center> MISS AYRAH NISAR </center></h1>")
def unni(request):
    return HttpResponse("<h1><center> Dr. NADEEM </center></h1>")
def vavac(request):
    return HttpResponse("<h1><center> Dr.NEIMAH </ center ></h1>")


# Create your views here.
