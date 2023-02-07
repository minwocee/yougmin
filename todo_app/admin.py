from django.contrib import admin
from .models import Todo
# Register your models here.



# 관리자 페이지에서 볼수 있게 한다.
admin.site.register(Todo)