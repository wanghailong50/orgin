from django.http import JsonResponse
from django.shortcuts import render,HttpResponse

import os,json

from artapp.models import Art
# Create your views here.

# 渲染文章的页面


from django.views.decorators.csrf import csrf_exempt

# 上传图片所需要的方法

def art_page(request):
    return render(request,'kindeditor.html')


@csrf_exempt
def art_img(request):
    file=request.FILES.get('imgFile')
    if file:
        Art.objects.create(img=file)
        img_url=request.scheme+"://"+request.get_host()+"/static/pic/"+str(file)
        print(img_url)
        result={"error":0,"url":img_url}
    else:
        result = {"error": 1, "url": "上传失败"}
    return JsonResponse(result)

# 获取所有的图片


def get_all_img(request):

    pic_dir=request.scheme+"://"+request.get_host()+'/static/'
    pic_list=Art.objects.all()


    rows=[]
    for i in list(pic_list):

        # 获取图片后缀
        path,pic_suffix=os.path.splitext(i.img.url)
        print(path,pic_suffix)
        rows.append({
            "is_dir":False,
            "has_file":False,
            "filesize":i.img.size,
            "dir_path":"",
            "is_photo":True,
            "filetype":pic_suffix,
            "filename":i.img.name,
            "datatime":"2018-06-06 00:36:2",
        })
    data={
        "moyeup_dir_path":"",
        "current_dir_path":"",
        "current_url":pic_dir,
        "totel_count":len(pic_list),
        "file_list":rows
    }
    return HttpResponse(json.dumps(data),content_type="application/json")

