from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post,Category

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','head_body','head_img',
            'body','category','price']

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Category)

admin.site.register(Post, PostAdmin)



