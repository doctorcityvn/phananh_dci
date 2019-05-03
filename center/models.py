from __future__ import unicode_literals
from django.db import models
from django import forms
from django.conf import settings
import django.utils.safestring as safestring
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.conf import settings
from django.contrib.auth import get_user_model


class LoggedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    tp = models.CharField("Thành phố:",default='', max_length=200, blank=True)

    def __unicode__(self):
        return self.user.username

    def login_user(sender, request, user, **kwargs):
        LoggedUser(user=user).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = LoggedUser.objects.get(user=user)
            u.delete()
        except LoggedUser.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class User0(models.Model):
    kh=models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ht= models.CharField("Họ tên:",default='', max_length=200, blank=True)
    dc = models.CharField("Địa chỉ:",default='', max_length=200, blank=True)
    tp = models.CharField("Thành phố:",default='', max_length=200, blank=True)
    mb = models.CharField("Mobile",default='', max_length=200,blank=True)
    em = models.CharField("Email:",default='', max_length=200, blank=True)
    def __str__(self):
        return self.ht



class Trang(models.Model):
    ttrang=models.Manager()
    name = models.CharField('tên trang:', max_length=10)


    def __str__(self):
        return self.name

class Division(models.Model):
    div=models.Manager()
    codediv = models.CharField("Code trung tâm",default='', max_length=10, primary_key=True)
    namediv = models.CharField('Tên trung tâm ', max_length=200)

    def __str__(self):
        return self.namediv
class Phongthuoctrungtam(models.Model):
    phongm=models.Manager()
    trungtam9=models.ForeignKey(Division, on_delete=models.CASCADE)
    maphong = models.CharField("Code phong",default='', max_length=10, primary_key=True)
    tenphong = models.CharField('Tên phong ',default='', max_length=200, blank=True)

    def __str__(self):
        return self.tenphong

class Bacsy(models.Model):
    bsy=models.Manager()
    codebs = models.CharField("Code:",default='', max_length=5, primary_key=True)
    hoten = models.CharField("Họ tên:",default='', max_length=200)
    diachi = models.CharField("Địa chỉ:",default='', max_length=200)
    thanhpho = models.CharField("Thành phố:",default='', max_length=200)
    mobile = models.CharField("Mobile",default='', max_length=200)
    email = models.CharField("Email:",default='', max_length=200)
    sochungchihanhnghe = models.CharField("Số Chứng chỉ hành nghề:",default='', max_length=200,blank=True,null=True)
    nghiepvu = models.CharField("Chuyên khoa",default='', max_length=200,blank=True,null=True)
    chucdanh = models.CharField("Chức danh",default='', max_length=200,blank=True,null=True)
    date = models.DateField(("Date ngày tham gia"), default=datetime.date.today)
    def __str__(self):
        return self.hoten

class Patient(models.Model):
    pat=models.Manager()
    khoa = models.ForeignKey(Division, on_delete=models.CASCADE)
    phong = models.ForeignKey(Phongthuoctrungtam, on_delete=models.CASCADE)
    bacsy = models.ForeignKey(Bacsy, on_delete=models.CASCADE,blank=True)
    codepatientp = models.CharField("Code bệnh nhân",default='BN1', max_length=10, primary_key=True)
    namepatient = models.CharField("Họ tên", max_length=200)
    age = models.IntegerField("Tuổi", default=40)
    place = models.CharField("Địa chỉ", max_length=200, null=True)
    City = models.CharField("Thành phố", max_length=200,default='Hà Nội', null=True)
    ordering = ['codepatientp']
    def __str__(self):
        return self.namepatient
class Medicine(models.Model):
    medi=models.Manager()
    codemedicine = models.CharField("Code medicine",default='K', max_length=200, primary_key=True)
    thc = models.CharField("Tên hoạt chất", default='',max_length=200)
    tbd = models.CharField("Tên biệt dược",default='', blank=True, null=True, max_length=200)
    dvt = models.CharField("Đơn vị tính",blank=True, default='',null=True, max_length=10)
    ttct = models.CharField("thông tin chi tiết", default='',blank=True, null=True,max_length=200)
    on_off=models.BooleanField(default=True)




    def __str__(self):
        return self.thc


class Typeservice(models.Model):

    typeserv=models.Manager()
    codeservice = models.CharField("Code service",default='DV', max_length=12, primary_key=True)
    name_serv = models.CharField(max_length=200)
    on_off=models.BooleanField(default=True)
    def __str__(self):
        return self.name_serv

class Service(models.Model):
    serv=models.Manager()
    codeservice = models.ForeignKey(Typeservice, on_delete=models.CASCADE)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField('Trạng thái', max_length=200,default='Đã gửi yêu cầu')
    lankham = models.CharField('Lần khám', max_length=3,default='1')
    date = models.DateField(("Ngày yêu cầu dịch vụ"), default=datetime.date.today)
    def __str__(self):
        return self.status
class Xlkhancap(models.Model):

    Xlkhancap1=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_xlkc = models.CharField('Tên xử lý khẩn cấp ', max_length=200)
    status = models.CharField('Trạng thái', max_length=200,default='Đã gửi yêu cầu')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.name_xlkc
class Typekhancap(models.Model):
    typekc=models.Manager()
    codekc = models.CharField("Code service",default='DV', max_length=12, primary_key=True)
    tenxlkc = models.CharField('Tên xử lý khẩn cấp ', max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    on_off=models.BooleanField(default=True)
    def __str__(self):
        return self.tenxlkc
class Donthuoc(models.Model):
    Donthuoc1=models.Manager()
    codedonthuoc = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    soluong = models.CharField('Số lượng ', max_length=200,default='1')
    huongdan = models.CharField('Hướng dẫn', max_length=255,default='')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.soluong

class Ketluan(models.Model):
    ketluan1=models.Manager()
    codeketluan = models.CharField("Code kết luận",default='', max_length=200, primary_key=True)
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name_ketluan = models.TextField('Kết luận ', blank=True,null=True)
    bacsy = models.CharField('Bác sỹ', max_length=200)
    lankham = models.CharField('Lần khám', max_length=3,default='1')
    date = models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return self.name_ketluan

class Trieuchung(models.Model):
    tchung=models.Manager()
    codetrieuchung = models.CharField("Code triệu chứng",default='', max_length=200, primary_key=True)
    trieuchung1 = models.CharField('Triệu chứng', max_length=200, default='Bất tỉnh')
    nhomcoquan = models.CharField('Nhóm cơ quan', max_length=200,default='Bất tỉnh')
    on_off=models.BooleanField(default=True)
    def get_first_image(self):
            return self.Trieuchungtq_set.all()
    def __str__(self):
        return self.trieuchung1

class Trieuchungtq(models.Model):
    trieuchungtqs=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='codepatienttctq')
    codetrieuchung = models.ForeignKey(Trieuchung, on_delete=models.CASCADE, related_name='codetctqs')
    status1 = models.CharField('Trạng thái', max_length=2,default='1')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Trieuchungcb(models.Model):
    tccucbo=models.Manager()
    codepatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    codetrieuchung = models.ForeignKey(Trieuchung, on_delete=models.CASCADE)
    status1 = models.CharField('Trạng thái', max_length=2,default='1')
    lankham = models.CharField('Lần khám',max_length=3,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Benhan(models.Model):
    ban=models.Manager()
    cba = models.CharField("Code:",default='', max_length=5, primary_key=True)
    bn = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bs = models.ForeignKey(Bacsy, on_delete=models.CASCADE)
    dnv = models.DateField(("Date ngày nhập viện"), default=datetime.date.today)
    dxv = models.DateField(("Date ngày xuất viện"), default=datetime.date.today)
    dttvp = models.DateField(("Date ngày thanh toán viện phí"), default=datetime.date.today)
class Trieuchungbenhnhan(models.Model):
    tcbn=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    ctt = models.ForeignKey(Trieuchung, on_delete=models.CASCADE)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status
class Xuly(models.Model):
    xl=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    txl = models.CharField('Tên xử lý khẩn cấp', max_length=200)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status
class Benhsu(models.Model):
    bs=models.Manager()
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    tbx = models.TextField('Tên bệnh sử', max_length=200)
    date = models.DateField("Ngày nhập dữ liệu:", default=datetime.date.today)
    def __str__(self):
        return self.tbx

class Dichvuyeucau(models.Model):
    dv=models.Manager()
    cdv= models.CharField("Code:",default='', max_length=5, primary_key=True)
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    tdv = models.CharField('Tên dịch vụ', max_length=200)
    tt = models.CharField('Trạng thái', max_length=2,default='1')
    date = models.DateField("Date", default=datetime.date.today)
    def __str__(self):
        return self.status1
class Donthuocdieutri(models.Model):
    dtdt=models.Manager()
    cdtdt = models.CharField("Code:",default='', max_length=5, primary_key=True)
    ct = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    cba = models.ForeignKey(Benhan, on_delete=models.CASCADE)
    sl = models.CharField('Số lượng ', max_length=200,default='1')
    dvt = models.CharField('Đơn vị tính', max_length=200,default='vỉ')
    date = models.DateField(("ngày kê đơn"), default=datetime.date.today)
    def __str__(self):
        return self.soluong

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]
class Yeucau(models.Model):
    yc=models.Manager()
    user = models.IntegerField()
    tdv = models.CharField('Tên dịch vụ',default='',blank=True, null=True, max_length=200)
    cl = models.CharField('Chất lượng', default='', max_length=20,blank=True, null=True)
    thanhtoan_v = models.CharField('thanhtoan', default="thanh toán bảo hiểm",blank=True, null=True,max_length=100)
    ma_thanhtoan_v=models.CharField('Mã thanh toan:',default='',blank=True, null=True, max_length=200)
    bs = models.CharField('bacsy', default='', max_length=20,blank=True, null=True)
    date = models.DateField("Ngày yêu cầu", default=datetime.date.today)
    def __str__(self):
        return self.tdv

class Quanlyuser(models.Model):
    qluser=models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin1= models.BooleanField(default=False)
    trungtam=models.ForeignKey(Division, on_delete=models.CASCADE,blank=True)
    phong=models.ForeignKey(Phongthuoctrungtam, on_delete=models.CASCADE,blank=True)
class Kieu_user(models.Model):
    kieuuser=models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    khachhang = models.BooleanField(default=False)
    bacsy = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    nhanvien_trungtam = models.BooleanField(default=False)
    nhanvien_data = models.BooleanField(default=False)



