import requests
from utils.random import ran
from cmfz_193 import settings
from redis import Redis
red = Redis(host='127.0.0.1',port=6379)

class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        # 使用云片网提供的第三方接口完成短信发送
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone):
        code=ran()
        parmas = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': "【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }
        req = requests.post(self.single_send_url, data=parmas)
        red.set(phone+'_1',code,120)
        print(req,code)


if __name__ == '__main__':
    yun_pian = YunPian(settings.API_KEY)
    yun_pian.send_message("15939035287")
