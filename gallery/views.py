from django.shortcuts import render, HttpResponse
import datetime as dt 

# Create your views here.
def welcome (request):
    return HttpResponse('BA PHOTO GALLERY')

def gallery_today(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)