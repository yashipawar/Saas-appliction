from django.http import HttpResponse
from django.shortcuts import render

from visits.models import Pagevisit


def home_page_view(request, *args, **kwargs):
    queryset = Pagevisit.objects.all()
    # return HttpResponse("<h1> hello </h1>")\
    name = "Yashi"
    info = {
        "name" : name,
        "queryset" : queryset.count()
    }
    Pagevisit.objects.create(path=request.path) # it'll store all the requests (page visits in path varible )
    return render(request, "home.html", info)