from django.contrib import admin

# Register your models here.

from django.contrib import admin

from NewsPortal.models import Post, Author, PostCategory, Category

# Register your models here.

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)