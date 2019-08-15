from django.shortcuts import render
from django.shortcuts import redirect
from home.models import User,Voice,Comment
from .form import UserForm
# Create your views here.
def home(request):
    voices = Voice.objects.all()
    return render(request, 'home.html', {"voices": voices})

def manage(request):
    playlists = Voice.objects.all()
    return render(request,'manage.html',{"playlists":playlists})

def uploads(requset):
    return render(requset,'uploads.html')

def register(request):
    if request.method == "POST":
        user = request.POST.get('user',None)
        password = request.POST.get('password',None)
        password2 = request.POST.get('password2',None)
        email = request.POST.get('email',None)
        name = request.POST.get('name',None)

        try:
            if User.objects.filter(account_number=user) :
                message = "此帳號已存在"
            else:
                if password != password2:
                    message = "兩次輸入的密碼不同!"
                else:
                    User.objects.create(account_number=user, password=password, email=email,name=name)
                    return redirect('/^home/')
        except:
            message = "發生錯誤!"
        return render(request, 'register.html', {"message": message})
    return render(request,'register.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/^home/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        #username = request.POST.get('username',None)
        #password = request.POST.get('password',None)
        message = "請填寫帳號和密碼"
        #if username and password :
        if login_form.is_valid():
            #username = username.strip()
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                userDB = User.objects.get(account_number=username)
                if userDB.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = username
                    request.session['user_name'] = userDB.name
                    return redirect('/^home/')
                else:
                    message = "密碼不正確"
            except:
                message="帳號輸入錯誤或不存在"
        return render(request,'login.html',{"message":message,"login_form":login_form})
    login_form = UserForm()
    return render(request,'login.html',{"login_form":login_form})

def logout(request):
    if not request.session.get('is_login'):
        return redirect('/^home/')  # 如果本来就未登录，也就没有登出一说
    else:
        request.session.flush()
        # 或者使用下面的方法
        # del request.session['is_login']
        # del request.session['user_id']
        # del request.session['user_name']
        return redirect("/^home/")

