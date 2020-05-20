from django.shortcuts import render

from django.http import HttpResponse

from htmlmin.decorators import minified_response

import feedparser


@minified_response
def index(request):

    if request.GET.get("url"):

        url = request.GET["url"] #Getting URL

        feed = feedparser.parse(url) #Parsing XML data   

        request.session['url'] = url

    else:

        feed = None
        
    return render(request, 'rss/reader.html', {'feed' : feed,})


@minified_response
def sort_asc(request):

    url= request.session['url']

    feed = feedparser.parse(url)    

   
    sorted_entries=sorted(feed.entries,key=lambda entry: entry['published_parsed'])   
    sorted_entries.reverse()
    feed['entries']=sorted_entries

    return render(request,'rss/reader.html', {'feed' : feed,})
    


@minified_response
def sort_desc(request):

    url= request.session['url']

    feed = feedparser.parse(url)  

    sorted_entries=sorted(feed.entries,key=lambda entry: entry['published_parsed'])   
    feed['entries']=sorted_entries

    return render(request,'rss/reader.html', {'feed' : feed,})


