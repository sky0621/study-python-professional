from django.shortcuts import render
from .models import Stock

# Create your views here.
def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/list.html', {'stocks': stocks})
