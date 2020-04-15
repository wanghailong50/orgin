from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from userapp.models import User
import json
import datetime

# Create your views here.


@csrf_exempt
def user_page(request):
    username=request.POST.get('username')
    religious_name=request.POST.get('religious_name')
    password=request.POST.get('password')
    salt=request.POST.get('salt')
    danger=request.POST.get('danger')
    head_pic=request.FILES.get('head_pic')
    print(head_pic)
    address=request.POST.get('address')
    signature=request.POST.get('signature')
    qq=request.POST.get('qq')
    phone=request.POST.get('phone')
    ts = datetime.datetime.now().timestamp()
    if username:
        user=User.objects.create(username=username,religious_name=religious_name,password=password,
                                 salt=salt,danger=danger,head_pic=head_pic,address=address,signature=signature
                                 ,qq=qq,phone=phone,resever=ts)
        user.save()

    return HttpResponse()


def get_all_user(request):
    user = User.objects.all().order_by('id')
    print(user[4].head_pic,34)
    rows = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page',1)  # 页吗
    all_page = Paginator(user, rows)
    try:
        page_obj = Paginator(user, rows).page(page).object_list
    except:
        page_obj = Paginator(user, rows).page(int(page) - 1).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,  # 总页码
        "records": all_page.count,  # 总数量
        "rows": list(page_obj)
    }

    def mydefalut(u):
        if isinstance(u, User):
            return {"id": u.id, "username": u.username, "religious_name": str(u.religious_name), "password": u.password, "salt": u.salt,
                    "danger":u.danger,"head_pic":u.head_pic.name,"address":u.address,"signature":u.signature,"phone":u.phone,"qq":u.qq}

    data = json.dumps(page_data, default=mydefalut)

    return HttpResponse(data)


def map_updata(request):
    return render(request, 'echars.html')


# 为前段图片提供数据
def load_map(request):
    users=User.objects.all()
    list1=[]
    y=['周一','周二','周三','周四','周五','周六','周天']
    ts = datetime.datetime.now().timestamp()
    count=0
    for i in users:
        print(i.resever)
        if ts-float(i.resever)<7*24*60*60:
            print(ts-float(i.resever))
            count+=1
    list1.append(count)
    data={
        "x":list1,
        "y":y,
    }
    return JsonResponse(data)


def map_updata2(request):
    return render(request, 'load_earth.html')


def load_earth(request):
    print(1111)
    users=User.objects.all()
    data=[]
    for i in users:
        data.append({'name':i.address,'value':1})
    '''{name: '北京',value: 34},
{name: '天津',value: 45},
{name: '上海',value: 32},
{name: '重庆',value: 22},
{name: '河北',value: 34},
{name: '河南',value: 56},
{name: '云南',value: 23},
{name: '辽宁',value: 34},
{name: '湖南',value: 23},
{name: '安徽',value: 24},
{name: '⼭东',value: 23},
{name: '新疆',value: 34},
{name: '江苏',value: 32},
{name: '浙江',value: 54},
{name: '江⻄',value: 23},
{name: '湖北',value: 32},
{name: '⼴⻄',value: 22},
{name: '⽢肃',value: 12},
{name: '⼭⻄',value: 33},
{name: '陕⻄',value: 23},
{name: '吉林',value: 34},
{name: '福建',value: 54},
{name: '贵州',value: 23},
{name: '⼴东',value: 45},
{name: '⻘海',value: 23},
{name: '⻄藏',value: 35},
{name: '四川',value: 45},
{name: '宁夏',value: 32},
{name: '海南',value: 43},
{name: '台湾',value: 54},
{name: '⾹港',value: 42},{name: '澳⻔',value: Math.round(Math.random()*1000)}'''

    return JsonResponse(data,safe=False)


def register(request):
    return render(request,'register.html')