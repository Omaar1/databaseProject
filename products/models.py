from __future__ import unicode_literals

from django.db import models
import json
from pprint import pprint




# Create your models here.
class Product(models.Model):  #Product Category
    category    = models.CharField(max_length=120 , null = True)
    courseUrl   = models.CharField(max_length=220,default="NotExist")
    duration    = models.CharField(max_length=120,default="10 weeks")
    image       = models.TextField(default="NotExist")
    name        = models.CharField(max_length=120, default="defaultCourse")
    price       = models.CharField(max_length=120 , default="10 AUD")
    promoMediaUrl       = models.TextField( default="NotExist")
    startDate           = models.CharField(max_length=120, default="15 Dec 2017" , null = True)
    summary             = models.TextField(default="NotExist")
    type                = models.CharField(max_length=120, default="free")
    instructorFullName  = models.CharField(max_length=120 , default="NotExist")
    instructorImageUrl  = models.CharField(max_length=220 ,default="NotExist")
    instructorProfileUrl = models.CharField(max_length=220,default="NotExist")



    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return self.title
# class Guestuser(models.Model):
#     name = models.CharField(max_length=120 , null = True, default = 'user')
#     joinedCourses = models.ForeignKey(Product, blank=True, null=True)

def parser():
    with open( 'E:\Dev\Courses\products\courseData.json') as data_file:
        data = json.load(data_file)
    # pprint(data)
    # line=line.decode('utf-8','ignore').encode("utf-8")
    return data

# 'F:\DevReal\eCommerce\src\courseData.json'

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''
