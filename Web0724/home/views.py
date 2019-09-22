from django.shortcuts import render
from django.shortcuts import redirect
from home.models import User,Voice,Comment,MySong
from .form import UserForm
from .YTgetData import YTGetData,YTSearchData
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from django.core.paginator import Paginator,PageNotAnInteger,InvalidPage,EmptyPage

# Create your views here.
def home(request):
    YT = YTGetData()
    voices = Voice.objects.all()
    if request.META.get('X-PJAX') == 'true':
        #return render(request, 'home.html', {"voices": voices, "pjax": 'true'})
        return render(request, 'home.html', {"voices": YT, "pjax": 'true'})
    else:
        #return render(request, 'home.html', {"voices": voices})
        return render(request, 'home.html', {"voices": YT})

def manage(request):
    playlists = Voice.objects.all()
    if request.META.get('X-PJAX') == 'true':
        return render(request,'manage.html',{"playlists":playlists,"user":str(request.session['user_id']),'pjax':'true'})
    else:
        return render(request, 'manage.html', {"playlists": playlists,"user":str(request.session['user_id'])})

def uploads(requset):
    return render(requset,'uploads.html')

def mylike(request):
    u = User.objects.get(account_number = str(request.session['user_id']) )
    mylikes = Voice.objects.filter(like=u)
    if request.META.get('X-PJAX') == 'true':
        return render(request,'mylike.html',{"mylikes":mylikes,"user":str(request.session['user_id']),'pjax':'true'})
    else:
        return render(request, 'mylike.html', {"mylikes": mylikes,"user":str(request.session['user_id'])})

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
        return redirect('/^home/login')  # 如果本来就未登录，也就没有登出一说
    else:
        request.session.flush()
        # 或者使用下面的方法
        # del request.session['is_login']
        # del request.session['user_id']
        # del request.session['user_name']
        return redirect("/^home/login")

def like_change(request):
    try:
        UserID = User.objects.get(account_number=str(request.session['user_id']))
        S_ID = request.GET.get('sid')
        SN = request.GET.get('SongName')
        likeYN = request.GET.get('likeYN')
        Song = Voice.objects.get(id=S_ID)
    except ObjectDoesNotExist:
        return ErrorResponse(401, 'object not exist')


    if likeYN == 'false':
        try:
            Song.like.add(UserID)
            return SuccessResponse('Y')
        except:
            return ErrorResponse(401,'not created')
    else:
        try:
            Song.like.remove(UserID)
            return SuccessResponse('N')
        except:
            return ErrorResponse(401,'not Deleted')

def AddSong(request):
    try:
        UserID = User.objects.get(account_number=str(request.session['user_id']))
        SN = request.GET.get('VoiceSongname')
        SID = request.GET.get('VoiceSrc')
        SA = request.GET.get('VoiceAuthor')
    except ObjectDoesNotExist:
        return ErrorResponse(401, 'object not exist')

    try:
        Voice.objects.get(Songname=SN)  #1.判斷是否在Voice裡，沒有就created
    except:
        try:
            Voice.objects.create(Songname=SN, song_src=SID, author=SA)
        except:
            return ErrorResponse(401, 'not created Voice')

    try:
        MySong.objects.get(User=UserID) #2.判斷使用者沒有歌單，先create
    except:
        try:
            MySong.objects.create(User=UserID)
        except:
            return ErrorResponse(401, 'not created UserSong')

    try:
        MySong.objects.get(User=UserID).Song.get(Songname=SN) #3.判斷使用者是否已add這首歌
        data = {
            'status': 'SUCCESS',
            'message':'歌單已經有這首歌了!'
        }

        return JsonResponse(data)
    except:
        try:
            MySong.objects.get(User=UserID).Song.add(Voice.objects.get(Songname=SN))
            data = {
                'status': 'SUCCESS',
                'message': '成功加入歌單'
            }
            return JsonResponse(data)
        except:
            return ErrorResponse(401, 'error done')


def SearchYT(request):
    try:
        Query = request.GET.get('Query')
        YT = YTSearchData(Query)
        YTlist = tuple(YT.items())
        paginator = Paginator(YTlist, 5)
        p = request.GET.get('page')
        try:
            SearchContent = paginator.page(p).object_list
            return JsonResponse(SearchContent,safe=False)
        except PageNotAnInteger:
            SearchContent = paginator.get_page(1)
        except EmptyPage:
            SearchContent = paginator.get_page(paginator.num_pages)
        except:
            return ErrorResponse(401,'error paginator')
    except:
        return ErrorResponse(401,'error Search')



def SuccessResponse(likeYN):
    data = {}
    data['status'] = 'SUCCESS'
    data['likeYN'] = likeYN
    return JsonResponse(data)

def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['message'] = message
    return JsonResponse(data)