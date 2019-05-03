from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Division, Patient, Service,Trieuchung, Trieuchungtq,Trieuchungcb, Ketluan, Xlkhancap,Donthuoc, Typeservice, Medicine
from .models import Benhan, Trieuchungbenhnhan, Xuly,Dichvuyeucau,Donthuocdieutri,Yeucau, User0, Typekhancap
from .models import Phongthuoctrungtam, Trang, Kieu_user, Quanlyuser, Bacsy,LoggedUser

from django.template import loader
from django.db.models import Q
from datetime import datetime
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.utils.encoding import force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
import getpass
from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def somathing():
   return something

def aj(request,slug):
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        kc =Typekhancap.typekc.all()
        sv =Typeservice.typeserv.all()
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Xlkc2 =Typekhancap.typekc.all()
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'Kluan1': Kluan1,
            'slug': slug,
            'Xlkc2':Xlkc2,
            'kc':kc,
            'phongweb':phongweb,

        }
        return render(request, 'center/test5.html', context)

def login1(request):
    user = request.POST.get('username')
    password = request.POST.get('password')
    user1 = authenticate(username=user, password=password)
    if user1 is not None:
        login(request, user1)
        hoten=getpass.getuser()
        q =Kieu_user.kieuuser.all().filter(user_id=user1.id)
        for kieu in q:
            if (kieu.khachhang):
                return redirect("http://doctorcityvn.pythonanywhere.com/menu_user/")
            if (kieu.bacsy):
                return redirect("http://doctorcityvn.pythonanywhere.com/menu_doctor/")
            if (kieu.nhanvien_trungtam):
                p =Quanlyuser.qluser.all().filter(user_id=user1.id)
                for k2 in p:
                    khoa3=''
                    phong3=''
                    person1 =Patient.pat.all().filter(khoa=khoa3, phong=phong3)
                    bacsy2 =Bacsy.bsy.all()
                    if (k2.phong_id == 'm24'):
                        person1 =Patient.pat.all().filter()
                    date1=datetime.date
                    namediv_list = Division.div.all()
                    phongweb =Phongthuoctrungtam.phongm.all().filter()
                    isname=request.POST.get("searchnamebn", "")

                    service1 =Service.serv.all().filter()
                    tctq =Trieuchungtq.trieuchungtqs.all().filter()
                    tccb =Trieuchungcb.tccucbo.all().filter()

                    tc =Trieuchung.tchung.all()
                    kc =Typekhancap.typekc.all()
                    sv =Typeservice.typeserv.all()
                    donthuoc1 =Donthuoc.Donthuoc1.all().filter()
                    dt =Medicine.medi.all()
                    Xlkc1 =Xlkhancap.Xlkhancap1.all().filter()
                    Xlkc2 =Typekhancap.typekc.all()
                    Kluan1 =Ketluan.ketluan1.all().filter()
                    isname=request.POST.get("searchnamebn", "")
                    person2 =Patient.pat.all().filter()
                    cname=''
                    cname2=''
                    phong_id="Phong A"
                    cname=request.POST.get("co1", "")
                    cname_0=request.POST.get("co_1", "")
                    cname2=request.POST.get("co2", "")
                    name3=request.POST.get("dv3", "")
                    dichvu_3=request.POST.get("sdichvu", "")
                    name4=request.POST.get("xlkc3", "")
                    nxlkc9=request.POST.get("xlkc_9", "")
                    ncb9=request.POST.get("cucbo_1", "")
                    context = {
                    'namediv_list': namediv_list,
                    'person1': person1,
                    'person2': person2,
                    'service1': service1,
                    'donthuoc1': donthuoc1,
                    'tctq': tctq,
                    'tccb': tccb,
                    'tc': tc,
                    'sv': sv,
                    'dt': dt,
                    'donthuoc1': donthuoc1,
                    'Xlkc1': Xlkc1,
                    'date1': date1,
                    'phong_id': phong_id,
                    'Kluan1': Kluan1,
                    'cname': cname,
                    'cname2': cname2,
                    'cname_0': cname_0,
                    'Xlkc2':Xlkc2,
                    'kc':kc,
                    'phongweb':phongweb,
                    'bacsy2': bacsy2,
                    'hoten':hoten,
                    }
                    return render(request, 'center/benhnhanall.html', context)
            if (kieu.nhanvien_data):
                return redirect("http://doctorcityvn.pythonanywhere.com/menu_data/")
            if (kieu.admin):
                return redirect("http://doctorcityvn.pythonanywhere.com/menu/")

    else:
        return render(request, 'center/login1.html')

def cacphong2(request,slug1, slug2):
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)

        tc =Trieuchung.tchung.all()
        kc =Typekhancap.typekc.all()
        sv =Typeservice.typeserv.all()
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Xlkc2 =Typekhancap.typekc.all()
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)
        cname=''
        cname2=''
        phong_id="Phong A"
        cname=request.POST.get("co1", "")
        cname_0=request.POST.get("co_1", "")
        cname2=request.POST.get("co2", "")
        name3=request.POST.get("dv3", "")
        dichvu_3=request.POST.get("sdichvu", "")
        name4=request.POST.get("xlkc3", "")
        nxlkc9=request.POST.get("xlkc_9", "")
        ncb9=request.POST.get("cucbo_1", "")


        if (cname):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname,status1=1,lankham=1)
            q.save()
        if (cname_0):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname_0,status1=1,lankham=1)
            q.save()
        if (cname2):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=cname2,status1=1,lankham=1)
            q.save()
        if (ncb9):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=ncb9,status1=1,lankham=1)
            q.save()
        if (name3):
            q=Service(codepatient_id=slug,codeservice_id=name3,status=1,lankham=1)
            q.save()
        if (dichvu_3):
            q=Service(codepatient_id=slug,codeservice_id=dichvu_3,status=1,lankham=1)
            q.save()
        if (name4):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=name4,status=1,lankham=1)
            q.save()
        if (nxlkc9):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=nxlkc9,status=1,lankham=1)
            q.save()
        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'Kluan1': Kluan1,
            'slug': slug,
            'cname': cname,
            'cname2': cname2,
            'cname_0': cname_0,
            'Xlkc2':Xlkc2,
            'kc':kc,
            'phongweb':phongweb,

        }
        return render(request, 'center/benhnhanthuocphong.html', context)
def Khoa(request):
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        iskhoa=request.POST.get("searchnamebn", "")

        person2 =Patient.pat.all().filter()
        context = {
            'namediv_list': namediv_list,
            'person2': person2,
            'phongweb':phongweb,
            'iskhoa': iskhoa,

        }
        return render(request, 'center/khoa.html', context)
def Khoa1(request,slug):
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter(trungtam9_id=slug)
        iskhoa=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(khoa_id=slug)
        context = {
            'namediv_list': namediv_list,
            'person2': person2,
            'phongweb':phongweb,
            'iskhoa': iskhoa,
            'slug': slug,

        }
        return render(request, 'center/khoa.html', context)


def signup2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("http://doctorcityvn.pythonanywhere.com/menu/")
    else:
        form = UserCreationForm()
        return render(request, 'center/signup1.html', {'form': form})
def sign_up(request):

    return render(request, 'center/sign_up.html')



def user1(request):
        current_user = request.user.get_full_name()
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'map1': map1,
            'current_user': current_user,


        }
        return render(request, 'center/user.html', context)




def Test(request):


        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        pancolor='#778899'
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        st1=""
        st2=""
        st3=""
        i1=1
        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1
                st1=" in active"
                st2=""
                st3=""


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenthuoc' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],name_medi=request.GET['tenthuoc'],dosage=request.GET['lieudung'],function1=request.GET['congdung_staff'], sideeffect=request.GET['tacdungphu'])
                q1.save()
                st2=" in active"
                st1=""
                st3=""


        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu'])
                q3.save()
                st3=" in active"
                st1=""
                st2=""


        else:
            message = 'You submitted an empty form.'
        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'st1': st1,
            'st2': st2,
            'date1': date1,
            'pancolor': pancolor,
            'map1': map1,



        }
        return render(request, 'center/test5.html', context)

def About(request):
        return render(request, 'center/about.html')

def map(request):
    return render(request, 'center/map.html')

def menu(request):
    return render(request, 'center/menu.html')

def menu_user(request):
    return render(request, 'center/menu_user.html')
def menu_doctor(request):
    return render(request, 'center/menu_doctor.html')
def menu_center(request):
    return render(request, 'center/menu_supportcenter.html')
def menu_data(request):
    return render(request, 'center/menu_data.html')


def Contact(request):
        return render(request, 'center/contact.html')
def Staff(request):
        current_user=""
        if not request.user.is_authenticated:
            return redirect('login1')
        else:
            current_user = request.user.get_full_name()
        namediv_list = Division.div.all()
        phong1=1
        person1 =Patient.pat.all()
        Xlkc1 =Typekhancap.typekc.all()
        dichvu5 =Typeservice.typeserv.all()
        khoa5 =Division.div.all()
        donthuoc5 =Medicine.medi.all()
        bncount = Patient.pat.all().count()+1
        tc =Trieuchung.tchung.all()
        trang9 =Trang.ttrang.get(pk=1)
        trang9.refresh_from_db()
        trang10=trang9.name
        thuoc=Medicine.medi.all()
        tccount=Trieuchung.tchung.all().count()
        date1=datetime.today()
        map1='AIzaSyD5wAflNNOYGLM4FiA9HWXZvYcPiyGi2sw'
        i1=1
        ttt=False
        txlkc=False
        tdv=False
        tdt=False
        tk=False
        if 'matrieuchung' in request.GET:
            if 'tentrieuchung' in request.GET:
                if 'nhomcoquan' in request.GET:
                    q=Trieuchung(codetrieuchung=request.GET['matrieuchung'],trieuchung1=request.GET['tentrieuchung'],nhomcoquan=request.GET['nhomcoquan'])
                    q.save()

                    bncount = Patient.pat.all().count()+1
                    ttt=True
                    trang9.name="tt"
                    trang9.save()
                    trang10=trang9.name


        else:
            message = 'You submitted an empty form.'
        if 'maxlkc' in request.GET:
            if 'tenxlkc' in request.GET:
                q=Typekhancap(codekc=request.GET['maxlkc'],tenxlkc=request.GET['tenxlkc'],date=datetime.today())
                q.save()
                txlkc=True
                trang9.name="xlkc"
                trang9.save()
                trang10=trang9.name


        else:
            message = 'You submitted an empty form.'

        if 'codestaff' in request.GET:
            if 'tuoistaff' in request.GET:

                q=Patient(Type_id_id=request.GET['phongidstaff'],codepatientp=request.GET['codestaff'],namepatient=request.GET['hotenstaff'],age=request.GET['tuoistaff'], place=request.GET['diachistaff'],City=request.GET['thanhphostaff'])
                q.save()
                bncount = Patient.pat.all().count()+1


        else:
            message = 'You submitted an empty form.'
        if 'codedonthuoc' in request.GET:
            if 'tenhoatchat' in request.GET:

                q1=Medicine(codemedicine=request.GET['codedonthuoc'],thc=request.GET['tenhoatchat'],tbd=request.GET['tenhoatchat'],dvt=request.GET['donvitinh'],ttct=request.GET['thongtinchitiet'],)
                q1.save()
                tdt=True
                trang9.name="dt"
                trang9.save()
                trang10=trang9.name




        else:
            message = 'You submitted an empty form.'

        if 'madichvu' in request.GET:
            if 'tendichvu1' in request.GET:

                q3=Typeservice(codeservice=request.GET['madichvu'],name_serv=request.GET['tendichvu1'])
                q3.save()
                tdv=True
                trang9.name="dv"
                trang9.save()
                trang10=trang9.name


        else:


            message = 'You submitted an empty form.'
        if 'makhoa' in request.GET:
            if 'tenkhoa' in request.GET:

                q3=Division(codediv=request.GET['makhoa'],namediv=request.GET['tenkhoa'])
                q3.save()
                tdv=True
                trang9.name="k"
                trang9.save()
                trang10=trang9.name


        else:


            message = 'You submitted an empty form.'

        context = {
            'namediv_list': namediv_list,
            'phong1': phong1,
            'person1': person1,
            'bncount': bncount,
            'tc': tc,
            'date1': date1,
            'map1': map1,
            'current_user': current_user,
            'ttt':ttt,
            'txlkc':txlkc,
            'tdv':tdv,
            'tdt':tdt,
            'tk':tk,
            'trang10':trang10,
            'Xlkc1':Xlkc1,
            'dichvu5':dichvu5,
            'khoa5':khoa5,
            'donthuoc5':donthuoc5,





        }
        return render(request, 'center/staff.html',context)







def print1(request,slug):
        date1=datetime.date
        year1=datetime.today().year
        month1=datetime.today().month
        day1=datetime.today().day

        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        person1 =Patient.pat.all().filter(codepatientp=slug)

        context = {
            'donthuoc1': donthuoc1,
            'slug':slug,
            'person1':person1,
            'date1':date1,
            'year1':year1,
            'month1':month1,
            'day1':day1,

        }
        return render(request, 'center/print1.html', context)
def cacphong1(request,slug):
        cname=''
        cname2=''
        phong_id="Phong A"
        cname=request.POST.get("co1", "")
        cname_0=request.POST.get("co_1", "")
        cname2=request.POST.get("co2", "")
        name3=request.POST.get("dv3", "")
        dichvu_3=request.POST.get("sdichvu", "")
        name4=request.POST.get("xlkc3", "")
        nxlkc9=request.POST.get("xlkc_9", "")
        ncb9=request.POST.get("cucbo_1", "")
        slthuoc=request.POST.get("soluongthuoc", "")
        tenthuoc1=request.POST.get("dt3", "")
        huongdansudung1=request.POST.get("huongdansudung", "")
        if (slthuoc):
            if (tenthuoc1):
                m1=Medicine.medi.all().filter(codemedicine=tenthuoc1)
                for m2 in m1:
                    qt=Donthuoc(codepatient_id=slug,codedonthuoc_id=m2.codemedicine,soluong=slthuoc,huongdan=huongdansudung1)
                    qt.save()
        if (cname):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname,status1=1,lankham=1)
            q.save()
        if (cname_0):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname_0,status1=1,lankham=1)
            q.save()
        if (cname2):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=cname2,status1=1,lankham=1)
            q.save()
        if (ncb9):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=ncb9,status1=1,lankham=1)
            q.save()
        if (name3):
            q=Service(codepatient_id=slug,codeservice_id=name3,status=1,lankham=1)
            q.save()
        if (dichvu_3):
            q=Service(codepatient_id=slug,codeservice_id=dichvu_3,status=1,lankham=1)
            q.save()
        if (name4):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=name4,status=1,lankham=1)
            q.save()
        if (nxlkc9):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=nxlkc9,status=1,lankham=1)
            q.save()
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        kc =Typekhancap.typekc.all()
        sv =Typeservice.typeserv.all()
      # u13=User.objects.all().filter(id=38).delete()

        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Xlkc2 =Typekhancap.typekc.all()
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)


        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'Kluan1': Kluan1,
            'slug': slug,
            'cname': cname,
            'cname2': cname2,
            'cname_0': cname_0,
            'Xlkc2':Xlkc2,
            'kc':kc,
            'phongweb':phongweb,

        }
        return render(request, 'center/benhnhan.html', context)
def thu1(request,slug):

        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        kc =Typekhancap.typekc.all()
        sv =Typeservice.typeserv.all()
        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Xlkc2 =Typekhancap.typekc.all()
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)


        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,

            'Kluan1': Kluan1,
            'slug': slug,

            'Xlkc2':Xlkc2,
            'kc':kc,
            'phongweb':phongweb,

        }
        return render(request, 'center/benhnhan_thu.html', context)

def alluser(request):
    users = User.objects.all()
    logged_users = LoggedUser.objects.all().order_by('user')
    context = {
        'users':users,
        'logged_users':logged_users,

    }
    return render(request, 'center/all_user.html', context)

def signup1(request):
    if request.method == 'POST':
        user1 = request.POST.get('username')
        password1 = request.POST.get('password')
        email1 = request.POST.get('email')
        hoten1= request.POST.get('firstname')

        gioitinh1 =request.POST.get('gender')
        diachi1 =request.POST.get('place')
        city1 =request.POST.get('city')
        mobile1 =request.POST.get('mobile')



        user = User.objects.create_user(user1, email1, password1)
        user.is_staff = True
        user.save()
        user = authenticate(username=user1, password=password1)
        if user is not None:

            q=User0(user_id=user.id,ht=hoten1,gioitinh=gioitinh1, dc=diachi1,tp=city1,mb=mobile1, em=email1)
            q.save()
            login(request, user)
            return redirect("http://doctorcityvn.pythonanywhere.com/menu/")
        else:
            return render(request, 'center/signup1.html')
    else:
        return render(request, 'center/signup1.html')

def validate_username(request):
    username2 = request.GET.get('username1', None)
    tendichvu_v= request.GET.get('tendichvu_w2', None)
    users=User.objects.get(username=username2)
    bacsy2 =Bacsy.bsy.all().filter(codebs='bs1')
    chatluong_v= request.GET.get('chatluong_w', None)
    ngonngu_v= request.GET.get('ngonngu_w', None)
    giadichvu_v= request.GET.get('giadichvu_w', None)
    hinhthucthanhtoan_v= request.GET.get('hinhthucthanhtoan_w', None)
    thanhtoandichvu_v= request.GET.get('thanhtoandichvu_w', None)
    q1=Yeucau(user=users.id,tdv=tendichvu_v,cl=chatluong_v,thanhtoan_v=hinhthucthanhtoan_v,ma_thanhtoan_v=thanhtoandichvu_v,bs='',date=datetime.today())
    q1.save()
    data = {
        'is_taken': username2
    }
    return JsonResponse(data)
def datlenh(request):
    yeucau =Yeucau.yc.all().filter()[:1]
    context = {
        'yeucau':yeucau,
    }
    return render(request, 'center/test5_yeucau.html',context)
def testnhanlenh(request):
    yeucau =Yeucau.yc.all().filter()[:1]
    context = {
        'yeucau':yeucau,
    }
    return render(request, 'center/test5_nhanlenh.html',context)

def Test5(request,slug):
        cname=''
        cname2=''
        phong_id="Phong A"
        cname=request.POST.get("co1", "")
        cname_0=request.POST.get("co_1", "")
        cname2=request.POST.get("co2", "")
        name3=request.POST.get("dv3", "")
        dichvu_3=request.POST.get("sdichvu", "")
        name4=request.POST.get("xlkc3", "")
        nxlkc9=request.POST.get("xlkc_9", "")
        ncb9=request.POST.get("cucbo_1", "")
        slthuoc=request.POST.get("soluongthuoc", "")
        tenthuoc1=request.POST.get("dt3", "")
        huongdansudung1=request.POST.get("huongdansudung", "")
        if (slthuoc):
            if (tenthuoc1):
                m1=Medicine.medi.all().filter(codemedicine=tenthuoc1)
                for m2 in m1:
                    qt=Donthuoc(codepatient_id=slug,codedonthuoc_id=m2.codemedicine,soluong=slthuoc,huongdan=huongdansudung1)
                    qt.save()
        if (cname):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname,status1=1,lankham=1)
            q.save()
        if (cname_0):
            q=Trieuchungtq(codepatient_id=slug,codetrieuchung_id=cname_0,status1=1,lankham=1)
            q.save()
        if (cname2):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=cname2,status1=1,lankham=1)
            q.save()
        if (ncb9):
            q=Trieuchungcb(codepatient_id=slug,codetrieuchung_id=ncb9,status1=1,lankham=1)
            q.save()
        if (name3):
            q=Service(codepatient_id=slug,codeservice_id=name3,status=1,lankham=1)
            q.save()
        if (dichvu_3):
            q=Service(codepatient_id=slug,codeservice_id=dichvu_3,status=1,lankham=1)
            q.save()
        if (name4):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=name4,status=1,lankham=1)
            q.save()
        if (nxlkc9):
            q=Xlkhancap(codepatient_id=slug,name_xlkc=nxlkc9,status=1,lankham=1)
            q.save()
        date1=datetime.date
        namediv_list = Division.div.all()
        phongweb =Phongthuoctrungtam.phongm.all().filter()
        isname=request.POST.get("searchnamebn", "")
        person1 =Patient.pat.all().filter(namepatient__icontains=isname)
        service1 =Service.serv.all().filter(codepatient_id=slug)
        tctq =Trieuchungtq.trieuchungtqs.all().filter(codepatient_id=slug)
        tccb =Trieuchungcb.tccucbo.all().filter(codepatient_id=slug)
        tc =Trieuchung.tchung.all()
        kc =Typekhancap.typekc.all()
        sv =Typeservice.typeserv.all()
      # u13=User.objects.all().filter(id=38).delete()

        donthuoc1 =Donthuoc.Donthuoc1.all().filter(codepatient_id=slug)
        dt =Medicine.medi.all()
        Xlkc1 =Xlkhancap.Xlkhancap1.all().filter(codepatient_id=slug)
        Xlkc2 =Typekhancap.typekc.all()
        Kluan1 =Ketluan.ketluan1.all().filter(codepatient_id=slug)
        isname=request.POST.get("searchnamebn", "")
        person2 =Patient.pat.all().filter(codepatientp=slug)


        context = {
            'namediv_list': namediv_list,
            'person1': person1,
            'person2': person2,
            'service1': service1,
            'donthuoc1': donthuoc1,
            'tctq': tctq,
            'tccb': tccb,
            'tc': tc,
            'sv': sv,
            'dt': dt,
            'donthuoc1': donthuoc1,
            'Xlkc1': Xlkc1,
            'date1': date1,
            'phong_id': phong_id,
            'Kluan1': Kluan1,
            'slug': slug,
            'cname': cname,
            'cname2': cname2,
            'cname_0': cname_0,
            'Xlkc2':Xlkc2,
            'kc':kc,
            'phongweb':phongweb,

        }
        return render(request, 'center/t5.html',context)

