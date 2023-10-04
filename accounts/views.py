from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):

    return render(request, 'accounts/index.html')

# 언제 로그인페이지 보여주고, 언제 로그인할지 구분하는거 =  HTTP 메서드로 구분
# 1. 로그인 페이지를 보여주고(GET)
# 2. 사용자가 입력했을 때, 실제 로그인 로직 수행(POST)
def login(request):
    # POST : 실제 로그인 로직 구현
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        # form에 있는 데이터가 유효하다면
        if form.is_valid():
            # 로그인 == 세션 ID 생성 및 등등을 장고가 제공.
            auth_login(request, form.get_user())
            return redirect('accounts:index')

    # GET : 로그인 페이지
    form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request,'accounts/login.html',context)

# 로그아웃 
# 세션 ID 삭제
def logout(request):
    auth_logout(request)
    return redirect("accounts:index")