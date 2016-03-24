from django.http import Http404
from django.shortcuts import render
from .models import Report

# Create your views here.


def report_detail(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report does not exist")
