import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


@csrf_exempt
def get_service(request):
    if request.method == "POST":
        resp = {'code': 1, 'msg': '调用服务成功', 'data': {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def get_judge(request):
    if request.method == "POST":
        resp = {'code': 1, 'msg': '调用服务成功', 'data': {}}
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}
    return HttpResponse(json.dumps(resp), content_type="application/json")