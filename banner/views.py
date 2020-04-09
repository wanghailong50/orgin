from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from banner.models import Slides
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def get_all_banner(request):
    """
    获取所有轮播图的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    Slides.objects.all()
    rows = request.GET.get('rows')  # 每页数量
    page = request.GET.get('page')  # 页吗

    slides = Slides.objects.all().order_by('id')
    all_page = Paginator(slides, rows)

    try:
        page_obj = Paginator(slides, rows).page(page).object_list
    except:
        page_obj = Paginator(slides, rows).page(int(page) - 1).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,  # 总页码
        "records": all_page.count,  # 总数量
        "rows": list(page_obj)
    }

    def mydefalut(u):
        if isinstance(u,Slides):

            return {"id":u.id,"name":u.title,"loaddata":str(u.loaddata),"isshow":u.isshow,"pic1":u.pic.name}

    data=json.dumps(page_data,default=mydefalut)

    return HttpResponse(data)


@csrf_exempt
def add_banner(request):
    title = request.POST.get("title")
    status = request.POST.get('status')
    if status=="1":
        status="展示"
    else:
        status="不展示"
    pic = request.FILES.get('pic')
    print(title, status, pic)
    sildes=Slides.objects.create(title=title,isshow=status,pic=pic)
    sildes.save()
    return HttpResponse()


@csrf_exempt
def del_data(request):
    id=request.POST.get('id')
    print(id)
    if id:
        slides=Slides.objects.get(id=id)
        slides.delete()

    return HttpResponse()

@csrf_exempt
def change(request):
    id=request.POST.get('id')
    upload_title=request.POST.get('upload_title')
    status=request.POST.get('status')
    upload_pic=request.FILES.get('upload_pic')

    slides=Slides.objects.get(id=int(id))
    slides.title=upload_title
    slides.pic=upload_pic
    if status == "1":
        status = "展示"
    else:
        status = "不展示"
    slides.isshow=status
    slides.save()
    return HttpResponse()