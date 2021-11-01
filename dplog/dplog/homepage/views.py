import json
import requests
from datetime import datetime
from django.shortcuts import render


def get_quotes():
    url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
    try:
        quote = requests.get(url).json()
    except ValueError as e:
        print('Quote ERROR')
        print(e)
        quote = json.loads('{"quoteText" : "Machines take me by surprise with great frequency.", "quoteAuthor" : "Alan Turing"}')
    return quote


def home(request):
    name = request.user.first_name
    date = datetime.today().strftime('%d %B')
    quotes = get_quotes()
    print('For error: '+str(quotes))
    quote = quotes['quoteText']
    quote_author = quotes['quoteAuthor']
    print(quotes)
    return render(
        request,
        'homepage/home.html',
        context={'name': name, 'date': date, 'quote': quote, 'quote_author': quote_author}
    )
