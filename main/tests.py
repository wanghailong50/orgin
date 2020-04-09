from django.test import TestCase
from django.http import HttpResponse
from django.shortcuts import render
from redis import Redis
from utils.send import YunPian
from cmfz_193 import settings
import re

red = Redis(host='127.0.0.1',port=6379)
red.set('name','666',10)