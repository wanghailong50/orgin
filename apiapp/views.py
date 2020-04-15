from django.shortcuts import render,HttpResponse
import json

from django.views.decorators.csrf import csrf_exempt

from banner.models import Slides
from artapp.models import Art
from userapp.models import User
# Create your views here.


def main_api(request):
    data=''
    user_id=request.GET.get('uid')
    type=request.GET.get('type')
    sub_type=request.GET.get('sub_type')

    if not user_id:
        data={
            "status":401,
            "msg":"请登录"
        }
        return HttpResponse(json.dumps(data))
    if type=="all":
        # 查询轮播图的相关信息
        slides=Slides.objects.all()
        slides_list=[]
        for i in slides:
            header={
                "title":i.title,
                "loaddata":i.loaddata,
                "pic":i.pic,
            }
            slides_list.append(header)

        data={
            "header":slides_list,     #轮播图信息
            "album":[],              #专辑相关信息
            "artical":[]                #文章相关信息
            }

    if type=="wen":
        data = {
            "album": [],  # 专辑相关信息
        }
    elif type=="si":
        arts=Art.objects.all()
        art_list=[]

        if sub_type=="ssyj":
            for i in arts:
                if i.title=="上师言教":
                    data={
                        "title":i.title,
                        "loaddata":i.loaddata,
                        "showdata":i.showdata,
                        "img":i.img,
                        "text":i.text,
                    }
                    art_list.append(data)
            data = {
                "artical":art_list   ,  # 上师言教的文章
            }
        else:
            for i in arts:
                if i.title=="显法密要":
                    data={
                        "title":i.title,
                        "loaddata":i.loaddata,
                        "showdata":i.showdata,
                        "img":i.img,
                        "text":i.text,
                    }
                    art_list.append(data)
            data = {
                "artical": [],  # 显法密要的文章
            }
    return HttpResponse(json.dumps(data))

@csrf_exempt
def register_api(request):
    phone=request.POST.get('phone')
    password=request.POST.get('password')

    user=User.objects.filter(phone=phone)

    if user:
        data={
            "error": "-200",
            "error_msg": "该手机号已经存在",
        }
        return HttpResponse(json.dumps(data))
    user_id=user[0].id
    data={
        "success":"200",
        "password": password,
        "uid": user_id,
        "phone ": phone # 手机号
    }
    return HttpResponse(json.dumps(data))


@csrf_exempt
def change_api(request):
    data=''
    user_id=request.POST.get('uid')
    user=User.objects.filter(id=user_id)[0]
    if user:
        gender = request.POST.get('gender')
        photo=request.POST.get('photo')
        location=request.POST.get('location')
        description=request.POST.get('description')
        nickname=request.POST.get('nickname')
        password=request.POST.get('password')

        phone=user.phone

        user.password=password
        user.danger=gender
        user.religious_name=nickname
        user.address=location
        user.signature=description
        user.head_pic=photo
        user.save()
        data={
            "password": password,
            "farmington": nickname, # 法名
            "uid": user_id, # 用户id
            "nickname": nickname, # 昵称
            "gender": gender, # 性别（m：男f：女）
            "photo": photo, # 头像
            "location": location, # 所在地
            "description": description, # 个人签名
            "phone ": phone # 手机号
        }
        return HttpResponse(json.dumps(data))
    data={
    "errno": "-200",
    "error_msg": "该手机号已经存在"
}
    return HttpResponse(json.dumps(data))
