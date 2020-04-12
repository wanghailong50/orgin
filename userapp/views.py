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