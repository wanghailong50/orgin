import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class Check_url(MiddlewareMixin):
    def process_request(self,request):
        current_url = request.path_info
        white_url=[
            '/main/login/',
            '/main/check_user',
            '/admin/.*',
        ]
        for i in white_url:
            if re.match(i,current_url):
                return None

        url_list=request.session.get('url_list')

        if not url_list:
            return HttpResponse("请登录")
        for url in url_list:
            if current_url==url:
                return None
        return HttpResponse('无权限')