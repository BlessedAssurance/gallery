from django.shortcuts import render, HttpResponse, Http404, redirect
import datetime as dt 

# Create your views here.
def welcome (request):
    return render(request, 'welcome.html')

def gallery_today(request):
    date = dt.date.today()
    return render(request, 'all-photos/today-photos.html', {"date": date,})



def past_days_gallery(request,past_date):
    # View Function to present news from past days:

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    return render(request, 'all-photos/past-photos.html', {"date": date})