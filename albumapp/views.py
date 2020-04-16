from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from albumapp.models import Album,Setcion
import json
# Create your views here.

# 查询数据库数据给前段表格用


def get_album(request):
    album=Album.objects.all().order_by('id')
    rows=request.GET.get('rows')   #每页数量
    page=request.GET.get('page',1)
    page_all=Paginator(album,rows)
    page_obj=page_all.page(page).object_list

    page_data={
        "page": page,
        "total": page_all.num_pages,  # 总页码
        "records": page_all.count,  # 总数量
        "rows": list(page_obj)
    }

    def mydefalut(u):
        if isinstance(u,Album):
            return {'ID':u.id,'name':u.name,'setcion_number':u.setcion_number,'publish':str(u.publish)}
    data=json.dumps(page_data,default=mydefalut)
    return HttpResponse(data)


def get_setcion(request):
    row_id=request.GET.get('row_id')
    rows=request.GET.get('rows') #每页数量
    page=request.GET.get('page')#总共多少也
    setcion=Setcion.objects.filter(album_id=row_id).order_by('id')
    page_all=Paginator(setcion,rows)
    page_obj=page_all.page(page).object_list
    page_data={
        "page":page,
        "total":page_all.num_pages,
        "records":page_all.count,
        "rows":list(page_obj)
    }

    def mydefalut(u):
        if isinstance(u,Setcion):
            return {'id':u.id,"setcion_name":u.setcion_name,"video_size":u.video_size,"video_time":str(u.video_time),"video_address":u.video_address}
    data=json.dumps(page_data,default=mydefalut)
    return HttpResponse(data)


@csrf_exempt
def add_viedo(request):
    redio_data=request.FILES.get('redio_data')
    redio_data='http://127.0.0.1:8002/static/'+str(redio_data)
    print(redio_data)
    redio=Setcion.objects.create(video_address=redio_data,album_id_id='1')
    redio.save()
    return HttpResponse()
