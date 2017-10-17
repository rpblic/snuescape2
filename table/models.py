from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
def datemake(pk):
    # pk: 1026
    pk= int(pk)
    return datetime.date(2017, pk//100, pk-100*(pk//100))

def timemake(pk):
    #pk: 11
    pk= int(pk)
    return datetime.time(pk, 00, 00)

class Rserv(models.Model):
    rserv_date= models.DateTimeField(
    primary_key= True
    )   #예약일자
    rserv_room= models.SmallIntegerField(default=2)
    reserved= models.BooleanField(
    verbose_name= "예약여부",
    default= False
    )   #예약여부
    applied= models.BooleanField(
    verbose_name= "확인여부",
    default= False
    )   #예약확인여부
    book_date= models.DateTimeField(
    verbose_name= "예약한날",
    default= timezone.now
    )   #신청일자
    rserv_er= models.CharField(
    verbose_name= "예약인",
    max_length= 200
    )         #예약인
    rserv_usernum= models.SmallIntegerField(
    verbose_name= "신청인원",
    default= 2
    ) #신청인원
    rserv_call= models.CharField(
    verbose_name="예약인 연락처",
    max_length= 20
    )        #예약인 전화번호

    # def book(self):
    #     self.rserv_date= timezone.now()
    #     self.reserved= True
    #     self.save()
    #
    # def apply(self):
    #     self.checked= True
    #     self.save()

    # def checker(self, rservs):
    #     for

    def __str__(self):
        return str(self.rserv_date)
