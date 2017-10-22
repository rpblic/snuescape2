from django.shortcuts import render, redirect
from .models import Rserv, datemake, timemake
from .forms import RservForm
from datetime import *
from django.contrib import messages

def timetable(request):
    return render(request, 'table/timetable.html', {})

def rserv_date(request, pk):
    date_pk= datemake(pk)
    rservs= Rserv.objects.filter(rserv_date__year= date_pk.year,\
                                rserv_date__month= date_pk.month,\
                                rserv_date__day= date_pk.day).exclude(reserved= False)

    rserv11_2= rservs.filter(rserv_date__hour= 11).filter(rserv_room= 2).exists()
    rserv12_2= rservs.filter(rserv_date__hour= 12).filter(rserv_room= 2).exists()
    rserv13_2= rservs.filter(rserv_date__hour= 13).filter(rserv_room= 2).exists()
    rserv14_2= rservs.filter(rserv_date__hour= 14).filter(rserv_room= 2).exists()
    rserv15_2= rservs.filter(rserv_date__hour= 15).filter(rserv_room= 2).exists()
    rserv16_2= rservs.filter(rserv_date__hour= 16).filter(rserv_room= 2).exists()
    rserv17_2= rservs.filter(rserv_date__hour= 17).filter(rserv_room= 2).exists()

    return render(request, 'table/rserv_date.html',\
                {'rservdate': pk, 'rserv11_2': rserv11_2, 'rserv12_2': rserv12_2, 'rserv13_2': rserv13_2,\
                'rserv14_2': rserv14_2, 'rserv15_2': rserv15_2, 'rserv16_2': rserv16_2,\
                 'rserv17_2': rserv17_2,  })

def rserv_info(request, rdate, pk, room):
    datetime_pk= datetime.combine(datemake(rdate), timemake(pk))
    if request.method== "POST":
        form= RservForm(request.POST)
        if form.is_valid():
            rserv= form.save(commit= False)
            rserv.rserv_date= datetime_pk
            rserv.rserv_room= room
            rserv.reserved= True
            rserv.save()
            messages.success(request, '예약되었습니다.')
            return redirect('timetable')
    else:
        form= RservForm()
    return render(request, 'table/rserv_info.html',\
            {'rservdatetime': datetime_pk, 'form': form})

def rserv_edit(request, rdate, pk):
    return None
