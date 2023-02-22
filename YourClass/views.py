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
""" def page_list(request):
    template = loader.get_template('page_list.html')
    posts = Post.objects.all().order_by('-Post_id').values()

    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request)) """
    
from django.views.generic import ListView

class PageListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'page_list.html'
    context_object_name = 'page_list'
    
    def get_querset(self):
        page_list = Post.objects.order_by('-Post_id')
        return page_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)
        
        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        
        start_index = int((current_page -1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index
        
        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        
        return context