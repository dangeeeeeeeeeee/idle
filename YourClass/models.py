from django.db import models

class Member(models.Model):
    email = models.TextField(primary_key=True) #id필드가 따로 생성되지 않게 함
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    rdate = models.DateTimeField()
    dept = models.CharField(max_length=10)
    fire = models.CharField(max_length=2)
    classname = models.ForeignKey('ClassNames', on_delete=models.CASCADE)

from uuid import uuid4

def get_file_path(instance, filename):
    uuid_name = uuid4().hex
    return uuid_name

class Post(models.Model):
    Post_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    file = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    date = models.DateTimeField()
    viewcount = models.TextField(default=0)
    email = models.ForeignKey('Member', on_delete=models.CASCADE)
    
class Comment(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    Post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    email = models.ForeignKey('Member', on_delete=models.CASCADE)
    
class Categories(models.Model):
    Cat_name = models.CharField(primary_key=True, max_length=20)
    Cat_info = models.TextField()
    
class ClassNames(models.Model):
    classnames = models.CharField(primary_key=True, max_length=30)