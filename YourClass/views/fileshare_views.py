from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from ..models import *

#대원 추가
from django.core.paginator import Paginator
def post_list(request):
    template = loader.get_template('post_list.html')
    page = request.GET.get('page', '1')  # 페이지
    posts = Post.objects.all().order_by('-Post_id').values()
    paginator = Paginator(posts, 5)  # 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'post_list': page_obj,
    }
    return HttpResponse(template.render(context, request))

from django.contrib import messages
def post_detail(request, Post_id):
    messages.info(request, "호오.. 게시글 내용을 보러오셨군요")
    template = loader.get_template('post_detail.html')

    post = Post.objects.get(Post_id=Post_id)
    context = {
        'post' : post
    }
    return HttpResponse(template.render(context, request))
    
from django.shortcuts import redirect
from ..forms import PostWriteForm 
from django.utils import timezone
def post_write(request):
    if request.method == "POST":
        form = PostWriteForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(**form.cleaned_data)
            # post = form.save(commit = False)
            # TODO models에서 옵션 auto_now=True로 바꾸고 아래 코드 주석처리 후 테스트
            nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            post.date = nowDatetime
            post.category = Categories.objects.get(Cat_name="자료실")
            post.email = Member.objects.get(email=request.session['login_'])
            if request.FILES:
                print("request.FILES 있음")
                if 'file' in request.FILES.keys():
                    post.filename = request.FILES['file'].name
            post.save()
            return redirect('post_list')
    else:
        form = PostWriteForm()
    context = {
        'form' : form
    }
    return render(request, 'post_write.html', context)

import urllib
import os
from django.http import Http404
import mimetypes
from django.shortcuts import get_object_or_404

def post_download(request, pk):
    post = get_object_or_404(Post, pk=pk)
    url = post.file.url[1:]
    file_url = urllib.parse.unquote(url)
    
    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(post.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404