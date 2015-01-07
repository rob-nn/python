from django.http import HttpResponse
from django.template import Context, Template
import datetime

def current_datetime(request):
    dt = datetime.datetime.now()
    fl = open('/home/roberto/Documents/python/django/djapp/djapp/mytemplate.html')
    template = Template(fl.read())
    fl.close()
    return HttpResponse(template.render(Context({'current_date': dt})))
    

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html= "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
