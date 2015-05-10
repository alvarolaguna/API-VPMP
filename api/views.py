from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import User, Report, ImageReport, Comment
from api.serializers import UserSerializer, ReportSerializer, ImageReportSerializer, CommentSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)

@csrf_exempt
def report_list(request):

    if request.method == 'GET':
        report = Report.objects.order_by('-missing_date')
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def user_report_detail(request, pk):

    user = User.objects.get(pk=pk)
    report  = Report.objects.filter(user_fk=user.pk)

    if request.method == 'GET':
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def report_detail(request, pk):

    try:
        report = Report.objects.get(pk=pk)
    except Report.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReportSerializer(report)  
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(report, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        report.delete()
        return HttpResponse(status=204)

@csrf_exempt
def report_image_detail(request, pk):

    report = Report.objects.get(pk=pk)
    image = Image.objects.filter(report_fk=report.pk)

    if request.method == 'GET':
        serializer = ImageSerializer(image, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def imageReport_list(request):

    if request.method == 'GET':
        imageReport = ImageReport.objects.all()
        serializer = ImageReportSerializer(imageReport, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ImageReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def imageReport_detail(request, pk):

    try:
        imageReport = ImageReport.objects.get(pk=pk)
    except ImageReport.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ImageReportSerializer(imageReport)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ImageReportSerializer(imageReport, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        imageReport.delete()
        return HttpResponse(status=204)

@csrf_exempt
def comment_list(request):

    if request.method == 'GET':
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def comment_detail(request, pk):

    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        comment.delete()
        return HttpResponse(status=204)

@csrf_exempt
def report_comment_detail(request, pk):

    report = Report.objects.get(pk=pk)
    comment = Comment.objects.filter(report_fk=report.pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def report_missingdate_filter(request, year, month, day):
    if missing_date != "":
	report= Report.objects.filter(missing_date <= missing_date)
   
    if request.method == 'GET':
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def report_name_filter(request):

    report = Report.objects.filter(name_subject = name_subject)

    if request.method == 'GET':
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

def report_status_filter(request, status):

    if status == "0":
	report = Report.objects.filter(status = "encontrado")
    elif status == "1":
        report = Report.objects.filter(status = "perdido")
    elif status == "2":
        report = Report.objects.filter(status = "albergue")

    if request.method == 'GET':
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

def report_gender_filter(request, gender):

    if gender == "0":
        report = Report.objects.filter(gender = "mujer")
    elif gender == "1":
        report = Report.objects.filter(gender = "hombre")

    if request.method == 'GET':
        serializer = ReportSerializer(report, many=True)
        return JSONResponse(serializer.data)

