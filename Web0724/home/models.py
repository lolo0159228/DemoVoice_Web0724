from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    gender =(
        ('male','男'),
        ('female','女')
    )
    account_number = models.CharField(max_length=20,blank=False,unique=True)
    name = models.CharField(max_length=10,blank=False)
    gender = models.CharField(max_length=10,choices=gender,default='male')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15,blank=False)
    createdate = models.DateTimeField(default=timezone.now)

class Voice(models.Model):
    Songname = models.CharField(max_length=50,blank=False,unique=True)
    author = models.CharField(max_length=50,blank=False)
    song_src = models.TextField(blank=False)
    introduce = models.TextField()
    like = models.ManyToManyField(to=User,blank=True)
    click = models.IntegerField(default=0)
    createdate = models.DateTimeField(default=timezone.now)
    updatedate = models.DateTimeField(default=timezone.now)

    def __str__(self):  #定義一個 __str__() 方法， 回覆 self.songname 值，這是在範本中此物件預設顯示的值，在 admin 介面亦顯示此值
        return self.Songname

    class Meta:
        ordering = ['-updatedate'] #從大到小排序

class Comment(models.Model):
    voice = models.ForeignKey(Voice,on_delete=models.CASCADE)  #on_delete=models.CASCADE 為 連串刪除
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    pubdate = models.DateTimeField(auto_now_add=True) #物件新增時自動設定為當時時間，設定之後即無法修改

    def __str__(self):
        return self.voice.Songname +'-'+str(self.id)  #將歌曲名稱串上該物件的 id

    class Meta:
        ordering = ['pubdate']

