from re import TEMPLATE
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def sayHello(Request):
    return render(Request, "sayHello.html")