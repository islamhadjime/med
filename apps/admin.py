from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post,Category,NumberUser,modelEmail

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title','head_body','head_img',
            'body','category','price']

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(NumberUser)
admin.site.register(Category)
admin.site.register(modelEmail)

admin.site.register(Post, PostAdmin)



