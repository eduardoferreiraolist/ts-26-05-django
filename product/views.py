from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_list(request):
    return render(request, 'product_list.html')

def product_form(request):
    return render(request, 'product_form.html')

def categories_list(request):
    return render(request, 'categories_list.html')

def categories_form(request):
    return render(request, 'categories_form.html')