from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def services(request):
    return render(request, 'main/services.html')

def blog(request):
    return render(request, 'main/blog.html')

def blog_single(request):
    return render(request, 'main/blog_single.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def portfolio_single(request):
    return render(request, 'main/portfolio_single.html')

def pricing(request):
    return render(request, 'main/pricing.html')
