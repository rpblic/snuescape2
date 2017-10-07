from django.shortcuts import render, get_object_or_404, redirect
from .models import Rserv, datemake, timemake
from django.utils import timezone
from .forms import RservForm
from datetime import *
from django.contrib import messages

def timetable(request):
    return render(request, 'table/timetable.html', {})

def rserv_date(request, pk):
    date_pk= datemake(pk)
    rservs= Rserv.objects.filter(rserv_date__year= date_pk.year,
                         rserv_date__month= date_pk.month,
                         rserv_date__day= date_pk.day).exclude(reserved= False)
    rserv11= rservs.filter(rserv_date__hour= 11)
    rserv12= rservs.filter(rserv_date__hour= 12)
    rserv13= rservs.filter(rserv_date__hour= 13)
    rserv14= rservs.filter(rserv_date__hour= 14)
    rserv15= rservs.filter(rserv_date__hour= 15)
    rserv16= rservs.filter(rserv_date__hour= 16)
    rserv17= rservs.filter(rserv_date__hour= 17)
    return render(request, 'table/rserv_date.html',\
                {'rservdate': pk, 'rserv11': rserv11, 'rserv12': rserv12, 'rserv13': rserv13, 'rserv14': rserv14, 'rserv15': rserv15, 'rserv16': rserv16, 'rserv17': rserv17, })

def rserv_info(request, rdate, pk):
    datetime_pk= datetime.combine(datemake(rdate), timemake(pk))
    if request.method== "POST":
        form= RservForm(request.POST)
        if form.is_valid():
            rserv= form.save(commit= False)
            rserv.rserv_date= datetime_pk
            rserv.reserved= True
            rserv.save()
            messages.success(request, '예약되었습니다.')
            return redirect('timetable')
    else:
        form= RservForm()
    return render(request, 'table/rserv_info.html', {'form': form})

def rserv_edit(request, rdate, pk):
    return None
