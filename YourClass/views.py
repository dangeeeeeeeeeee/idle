from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

from django.http import HttpResponse # 대원 추가


#메인페이지
def index(request):
    template = loader.get_template('index.html')
    member = Member.objects.values()
    context = {
        'member' : member
    }
    request.session['login_'] = "hong@gmail.com"
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

#대원 추가
from django.core.paginator import Paginator
def post_list(request):
    template = loader.get_template('post_list.html')
    page = request.GET.get('page', '1')  # 페이지
    posts = Post.objects.all().order_by('-Post_id').values()
    paginator = Paginator(posts, 2)  # 페이지당 2개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'post_list': page_obj,
    }
    return HttpResponse(template.render(context, request))

def post_detail(request, Post_id):
    template = loader.get_template('post_detail.html')

    post = Post.objects.get(Post_id=Post_id)
    context = {
        'post' : post
    }
    return HttpResponse(template.render(context, request))
    
# from .models import Post
# from .models import Member
from django.shortcuts import redirect
from .forms import PostWriteForm

def post_write(request):
    if request.method == "POST":
        form = PostWriteForm(request.POST)
        user = request.session['login_']
        user_id = Member.objects.get(email = user)

        if form.is_valid():
            post = form.save(commit = False)
            post.writer = user_id
            post.save()
            return redirect('post:post_list')
    else:
        form = PostWriteForm()

    return render(request, "post_write.html", {'form': form})
