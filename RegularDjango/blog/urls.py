from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


from blog.views import (

	BlogEditorView,
    TestView,
    BlogUploaderView,
    BlogEditorView,
    BlogRemoverView,
    BlogView,
    BlogHomeView

)

app_name = "blog"

urlpatterns =[
    path('', BlogHomeView, name='home'),
    path('blog-editor/<str:pk>', BlogEditorView , name = 'blog_editor'),
    path('test/', TestView, name="test"),
    path('blog_uploader/', login_required(BlogUploaderView), name="uploader"),
    path('blog/<str:pk>', BlogView, name="view_blog"),
    path('blog/delete/<str:pk>', BlogRemoverView, name="blog_delete")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)