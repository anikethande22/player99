from django.shortcuts import render

# Create your views here.
def home(request):
    print("Welcoem to Home Page")
    return render(request,'home.html')

def aboutus(request):
    print(aboutus)
    return render(request,'aboutus.html')
