from django.contrib import admin
from .models import User,Voice,Comment
# Register your models here.

class Useradmin(admin.ModelAdmin):
    list_display = ('account_number','name','gender','email','password','createdate')

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['voice','comment','pubdate']
    list_display_links = ['voice'] #設定資料連結欄位,透過voice來連結
    list_filter = ['voice','comment'] #設定右方過濾欄位為 article 與 content，點選即可濾出該項目的相關資料
    search_fields = ['comment']

    class Meta: #是一個類別容器 (Class container)，內含有關該類別的詮釋資料 (稱為 Metadata)，例如：排序、權限、所使用的 Model 等
        model = Comment

admin.site.register(User,Useradmin)
admin.site.register(Voice)
admin.site.register(Comment,CommentModelAdmin)