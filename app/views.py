from django.shortcuts import render

# Create your views here.

def first_jinja(request):
    d={'name':'karthik','age':21}
    return render(request,'jinja_printing.html',context=d)