from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

#메인페이지
def index(request):
    template = loader.get_template('index.html')
    member = Member.objects.values()
    context = {
        'member' : member
    }
    return HttpResponse(template.render(context, request))
   
#회원가입
def signup():
    pass

#로그인 (로그인 성공하여 리다이렉트시 models.py의 Member객체가 전부 함께 넘어가야합니당)
def login():
    pass

#마이페이지(로그인시 메인에서 ~~님 눌렀을 때 화면)
def mypage():
    pass

#회원정보수정(마이페이지에서 정보수정 눌렀을때화면)
def editinfo():
    pass

#일정
def calendar():
    pass

#게시판 (일단 게시판1, 게시판2,.. 이런식으로 하고 나중에 수정할게유)
def board1():
    pass