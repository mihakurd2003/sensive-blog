from django.contrib import admin
from blog.models import Post, Tag, Comment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text', 'published_at']
    raw_id_fields = ['post', 'author']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']


class PostTagInline(admin.TabularInline):
    model = Post.tags.through
    raw_id_fields = ['post']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [PostTagInline]


admin.site.unregister(User)


class PostLikesInline(admin.TabularInline):
    model = Post.likes.through
    verbose_name_plural = 'Лайки'
    raw_id_fields = ['user']


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [PostLikesInline]




