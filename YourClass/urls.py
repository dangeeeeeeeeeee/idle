from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('mypage/', views.mypage, name='mypage'),
    path('editinfo/', views.editinfo, name='editinfo'),
    path('calendar/', views.calendar, name='calendar'),
    path('board1/', views.board1, name='board1'), 
    
    ########################################################
    
    path('postList/', views.post_list, name='post_list'), 
]