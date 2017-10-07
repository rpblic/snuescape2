from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
def datemake(pk):
    # pk: 1026
    pk= int(pk)
    return datetime.date(2017, pk//100, pk-100*(pk//100))

def timemake(pk):
    pk= int(pk)
    return datetime.time(pk, 00, 00)

class Rserv(models.Model):
    rserv_date= models.DateTimeField(
    primary_key= True
    )
    reserved= models.BooleanField(
    default= False
    )
    applied= models.BooleanField(
    default= False
    )
    book_date= models.DateTimeField(
    default= timezone.now
    )
    rserv_er= models.CharField(max_length= 200)
    rserv_call= models.CharField(max_length= 20)

    def book(self):
        self.rserv_date= timezone.now()
        self.reserved= True
        self.save()

    def apply(self):
        self.checked= True
        self.save()
        #save로 해야 되나? modify 같은 걸 할 수 있으려나?

    # def checker(self, rservs):
    #     for

    def __str__(self):
        return self.title
