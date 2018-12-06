from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post,Tag,Category


class PostAdmin(admin.ModelAdmin):
	list_display = ['title','created_time','modified_time','category','author']
	class Media:
		js = (
		'/static/js/kindeditor-4.1.10/kindeditor-min.js',
		#'/static/js/kindeditor-4.1.10/kindeditor.js',
		'/static/js/kindeditor-4.1.10/lang/zh_CN.js',
		'/static/config.js',
		 
		'/static/blog/js/jquery-2.1.3.min.js',
		
		)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)