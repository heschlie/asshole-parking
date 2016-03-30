from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Report


# Create your views here.


def index(request):
    latest_reports = Report.objects.order_by('-submit_date')[:5]

    return render(request, 'index.html', {'reports': latest_reports})


def report_list(request):
    latest_reports = Report.objects.order_by('-submit_date')

    return render(request, 'report_list.html', {'reports': latest_reports})


def report_detail(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report does not exist")

    return render(request, 'report_detail.html', {'report': report})
