from django.shortcuts import render

def events(request):
    return render(request,'gallery/events.html')


# Create your views here.
def product(request):
    return render(request,'gallery/product.html')  #no need to include template in the path
def flowers(request):
    return render(request,'gallery/flowers.html')


