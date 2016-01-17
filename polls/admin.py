from django.contrib import admin

from .models import Post,Comment,Image

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Відредагувати інформацію',{'fields':['post_header']}),
        (None,                 {'fields': ['posts_auftor_name']}),
        (None,                 {'fields': ['post_text']}),
        ('Налаштувати дату публікації',{'fields':['pub_date'],'classes':['collapse']})
    ]

    inlines = [CommentInline,ImageInline]

    list_display = ('post_header','pub_date')

admin.site.register(Post,PostAdmin)

# Register your models here.
