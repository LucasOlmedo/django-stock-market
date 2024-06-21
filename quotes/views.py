from django.shortcuts import render, redirect
import json
import requests
import os
from dotenv import load_dotenv
from .models import Stock
from .forms import StockForm
from django.contrib import messages

load_dotenv()

# Create your views here.

API_URL = "https://finnhub.io/api/v1"
TOKEN = os.getenv("API_KEY_FINNHUB")


def api_get_stocks(ticker):
    api_request = requests.get(
        API_URL+"/stock/profile2?symbol=" + ticker+"&token="+TOKEN)
    try:
        return json.loads(api_request.content)
    except Exception as e:
        return {}


def home(request):

    if request.method == "POST":
        result = api_get_stocks(ticker=request.POST['ticker'])
        return render(request, 'home.html', {'result': result})
    else:
        return render(request, 'home.html', {
            'ticker': "Enter a ticker to get quote"
        })


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Added"))
            return redirect('add_stock')
    else:
        output = []
        stocks = Stock.objects.all()
        for item in stocks:
            result = api_get_stocks(item.ticker)
            if not result:
                pass
            else:
                output.append(result)
        return render(request, 'add_stock.html', {
            'stocks': stocks,
            'output': output
        })


def delete(request, pk):
    stock = Stock.objects.get(pk=pk)
    stock.delete()
    messages.success(request, ("Stock Deleted"))
    return redirect('add_stock')
