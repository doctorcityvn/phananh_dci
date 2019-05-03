from __future__ import unicode_literals
from django.contrib import admin
from .models import user2
class user2ModelAdmin(admin.ModelAdmin):
    #inlines = [TrieuchungtqInLine, TrieuchungcbInLine]
    list_display = ('user', 'bio','location', 'birth_date')
# Register your models here.
admin.site.register(user2, user2ModelAdmin)