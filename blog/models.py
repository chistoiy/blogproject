# coding: utf-8


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
		
from django.utils.html import strip_tags
class Post(models.Model):
	title = models.CharField(max_length=70)
	body = models.TextField()
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()
	excerpt = models.CharField(max_length=200,blank=True)#摘要，允许为空
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,)
	# 新增 views 字段记录阅读量
	views = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})
	class Meta:
		ordering = ['-created_time','title']
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])
		
	def save(self, *args, **kwargs): 
		 
        # 如果没有填写摘要
		if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
			md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
			self.excerpt = strip_tags(md.convert(self.body))[:54]
		#self.body = strip_tags(md.convert(self.body))
        # 调用父类的 save 方法将数据保存到数据库中
		#print('测试保存的重载！')
		super(Post, self).save(*args, **kwargs)
	
	def delete(self,*args,**kwargs):
		#print('测试删除函数的重载！！！！！！！！！！')
		#print(self.id)
		
		super(Post, self).delete(*args, **kwargs)
		 
		import os
		import shutil
		path = 'static/media/article/%s/'%self.id
		if os.path.exists(path):
			shutil.rmtree(path)
			