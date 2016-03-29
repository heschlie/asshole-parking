from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Report


# Create your views here.


def index(request):
    return HttpResponse('Welcome home.')


def report_list(request):
    reports = Report.objects.all()
    reports_string = ''
    for report in reports:
        reports_string += \
            '{}, {}, reported by: {}<br>'.format(report.title,
                                                 report.violation,
                                                 report.reporter)

    return HttpResponse(reports_string)


def report_detail(request, report_id):
    try:
        report = Report.objects.get(pk=report_id)
    except Report.DoesNotExist:
        raise Http404("Report does not exist")

    return render(request, 'report_detail.html', {'report': report})
