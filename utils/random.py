from django.test import TestCase
import random



def ran():
    list = ''
    for i in range(4):
        result = random.randrange(0, 4)
        list = list + str(result)
    return list