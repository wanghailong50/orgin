from django.http import HttpResponse
from django.shortcuts import render
from redis import Redis
from utils.send import YunPian
from cmfz_193 import settings
import re

red = Redis(host='127.0.0.1',port=6379)
red.set('name','666',10)

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cmfz_193.settings import API_KEY
from utils.send import YunPian


def index(request):
    return render(request, "main.html")


def login_form(request):
    return render(request, "login.html")


@csrf_exempt
def get_code(request):
    """
    接受前端发送的ajax请求并为手机号发送验证码
    :param request: 用户输入的数据号
    :return: None
    """
    mobile = request.POST.get("mobile")
    MOBILE = "^1[358]\d{9}$|^147\d{8}$|^179\d{8}$"
    p = re.compile(MOBILE)

    if p.match(mobile):
        yun_pian = YunPian(settings.API_KEY)
        yun_pian.send_message(mobile)

        return HttpResponse("success")
    return HttpResponse("over")

    # 获取手机号有没有对应的验证码 查看验证码是否在120S内  如果在  提示验证码已经发送
    # value = redis.get("18500230996_1")  如果返回的值存在  代表120s之内还不能发送

    # 判断手机号是否存在  正则验证是否合法
    # if mobile:
    #     yun_pian = YunPian(API_KEY)
    #     yun_pian.send_message(mobile)
        # 将手机号与对应的验证码存入redis  防止无限制发送
        # redis.set("18500230996_1", "666666", 120S)
        # 保证验证码的有效期
        # redis.set("18500230996_2", "666666", 600s)



def check_user(request):
    """
    用户登录信息校验的视图
    :param request: 表单数据
    :return:
    """
    mobile = request.GET.get('mobile')
    code = request.GET.get('code')

    if  red.get(mobile+'_1'):
        if str(red.get(mobile+'_1'),encoding='utf-8')==code:

            return HttpResponse('success')
    return HttpResponse('over')

    # 校验信息是否合法
    # 验证码是否在有效期内  使用redis
    # redis.get("18500230996_2")


