from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func , ingest_data_from_excel


# Create your views here.
def test(request):
    ingest_data_from_excel.delay()
    return HttpResponse("Done")