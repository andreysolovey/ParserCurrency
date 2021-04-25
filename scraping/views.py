from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from scraping.models import Job


class Index(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        items = Job.objects.all()
        return render(request, 'lol.html', {'items': items})
