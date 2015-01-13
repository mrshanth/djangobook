from django.http import HttpResponse
import datetime

def blah(request):
    return HttpResponse("This is even more Blah!")

def hello(request):
    return HttpResponse("Hello World")

def timenow(request):
    now = datetime.datetime.now()
    html = "<html><body>Time: %s </body> </html>" %now
    return HttpResponse(html)

def time_calc(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)
