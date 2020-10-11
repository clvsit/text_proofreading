import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")


@csrf_exempt
def get_service(request):
    print(request.method)
    if request.method == "POST":
        resp = {
            'code': 1,
            'msg': '调用服务成功',
            'data': {
                "answerList": [
                    {"id": "60e38bfe7af14d7c96c586cc3443a7f7", "start": 0, "end": 3, "answer": "成都", "source": "程度",
                     "type": "0"},
                    {"id": "96873e8dcf074405963b6f9b9ab02dc6", "start": 0, "end": 3, "answer": "篮", "source": "蓝",
                     "type": "0"},
                    {"id": "b16845bfc12744f591b9c4ed22ec5f74", "start": 0, "end": 3, "answer": "考虑", "source": "考虑考虑",
                     "type": "1"}
                ]
            }
        }
    else:
        resp = {"code": 0, "msg": "请求方法有误！", "data": {}}
    return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def get_judge(request):
    resp = {'code': 1, 'msg': '调用服务成功', 'data': {
        "answerList": [
            {id: "60e38bfe-7af1-4d7c-96c5-86cc3443a7f7", "start": 0, "end": 3, "answer": "成都", "source": "程度", type: 0},
            {id: "96873e8d-cf07-4405-963b-6f9b9ab02dc6", "start": 0, "end": 3, "answer": "篮", "source": "蓝", type: 0},
            {id: "b16845bf-c127-44f5-91b9-c4ed22ec5f74", "start": 0, "end": 3, "answer": "考虑", "source": "考虑考虑",
             type: 1},
        ]
    }}

    return HttpResponse(json.dumps(resp), content_type="application/json")
