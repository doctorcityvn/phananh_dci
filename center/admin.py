from __future__ import unicode_literals

from django.contrib import admin
from .models import Division, Patient, Service, Trieuchung, Trieuchungtq, Trieuchungcb, Ketluan, Xlkhancap, Donthuoc, Typeservice, Medicine
from .models import Bacsy, Phongthuoctrungtam, Quanlyuser
from .models import Benhan, Trieuchungbenhnhan, Xuly,Dichvuyeucau,Donthuocdieutri,Yeucau, User0, Benhsu,Typekhancap, Trang,Kieu_user, LoggedUser

class TrieuchungcbInLine(admin.StackedInline):
    model = Trieuchungcb
    extra = 1

class TrieuchungtqInLine(admin.StackedInline):
    model = Trieuchungtq
    extra = 1
class KetluanInLine(admin.StackedInline):
    model = Ketluan
    extra = 1
class ServiceInLine(admin.StackedInline):
    model = Service
    extra = 1
class XlkhancapInLine(admin.StackedInline):
    model = Xlkhancap
    extra = 1
class DonthuocInLine(admin.StackedInline):
    model = Donthuoc
    extra = 1

class TrieuchungModelAdmin(admin.ModelAdmin):
    list_display = ('codetrieuchung','trieuchung1','nhomcoquan' )

class TrieuchungtqModelAdmin(admin.ModelAdmin):
    list_display = ('codepatient','codetrieuchung','status1','lankham','date','codepatient_id'  )
class TrieuchungcbModelAdmin(admin.ModelAdmin):
    list_display = ('codepatient','codetrieuchung','status1','lankham','date','codepatient_id'  )

class ServiceModelAdmin(admin.ModelAdmin):

    list_display = ('codeservice','codepatient_id','status','lankham','date' )

class TypeserviceModelAdmin(admin.ModelAdmin):

    list_display = ('codeservice','name_serv'  )
class XlkhancapModelAdmin(admin.ModelAdmin):

    list_display = ('codepatient','name_xlkc','status', 'lankham','date', 'codepatient_id'  )
class TypekhancapModelAdmin(admin.ModelAdmin):

    list_display = ('codekc','tenxlkc','date')

class MedicineModelAdmin(admin.ModelAdmin):

    list_display = ('codemedicine','thc','tbd','dvt', 'ttct')

class DonthuocModelAdmin(admin.ModelAdmin):

    list_display = ('codedonthuoc','codepatient_id','soluong','date')

class KetluanModelAdmin(admin.ModelAdmin):
    list_display = ('bacsy','codepatient','lankham','date', 'name_ketluan','codepatient_id'  )



class DivisionModelAdmin(admin.ModelAdmin):

    list_display = ('codediv','namediv' )



class PatientModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('khoa','phong','codepatientp', 'namepatient', 'age','place','City','bacsy')
class BacsyModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('codebs', 'hoten', 'diachi','thanhpho','mobile','email','sochungchihanhnghe','nghiepvu','chucdanh','date')
class User0ModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('user', 'ht', 'dc','tp','mb','em')
class YeucauModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('user', 'tdv','cl','thanhtoan_v','ma_thanhtoan_v','bs','date')
class DonthuocdieutriModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cdtdt', 'ct', 'cba','sl','dvt','date')
class DichvuyeucauModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cdv', 'cba', 'tdv','tt','date')

class XulyModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cba', 'txl','tt','date')

class TrieuchungbenhnhanModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cba', 'ctt','tt','date')

class BenhanModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cba', 'bn','bs','nnv','nxv','nttvp')

class BenhsuModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('cba', 'tbx','date')

class PhongthuoctrungtamModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('maphong', 'tenphong', 'trungtam9')
class TrangModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('id','name')
class QuanlyuserModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('user','admin1', 'trungtam', 'phong')

class Kieu_userModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('user','khachhang', 'bacsy','nhanvien_trungtam', 'nhanvien_data')

class LoggedUserModelAdmin(admin.ModelAdmin):

    list_display = ('user','tp')


admin.site.register(LoggedUser, LoggedUserModelAdmin)
admin.site.register(Trang, TrangModelAdmin)
admin.site.register(Phongthuoctrungtam, PhongthuoctrungtamModelAdmin)
admin.site.register(Benhsu, BenhsuModelAdmin)
admin.site.register(Trieuchungbenhnhan, TrieuchungbenhnhanModelAdmin)
admin.site.register(Xuly, XulyModelAdmin)
admin.site.register(Dichvuyeucau, DichvuyeucauModelAdmin)
admin.site.register(Donthuocdieutri, DonthuocdieutriModelAdmin)
admin.site.register(Yeucau, YeucauModelAdmin)
admin.site.register(User0, User0ModelAdmin)
admin.site.register(Bacsy, BacsyModelAdmin)

admin.site.register(Donthuoc, DonthuocModelAdmin)
admin.site.register( Medicine, MedicineModelAdmin)
admin.site.register(Division, DivisionModelAdmin)
admin.site.register(Patient, PatientModelAdmin)
admin.site.register(Service, ServiceModelAdmin)
admin.site.register(Typeservice, TypeserviceModelAdmin)
admin.site.register(Ketluan, KetluanModelAdmin)
admin.site.register(Xlkhancap, XlkhancapModelAdmin)
admin.site.register(Typekhancap, TypekhancapModelAdmin)
admin.site.register(Trieuchungtq, TrieuchungtqModelAdmin)
admin.site.register(Trieuchungcb, TrieuchungcbModelAdmin)
admin.site.register(Trieuchung, TrieuchungModelAdmin)
admin.site.register(Quanlyuser, QuanlyuserModelAdmin)
admin.site.register(Kieu_user, Kieu_userModelAdmin)
