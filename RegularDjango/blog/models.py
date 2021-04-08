from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

def blog_images_path(instance, filename):
    return 'blogs/{}/{}'.format(instance.title, instance.author)
    
class BlogUploaderModel(models.Model):

    title = models.CharField(max_length =  200)
    body = RichTextUploadingField(blank=True)
    abstract = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to=blog_images_path)
    issue_date = models.DateField(auto_now_add=True)
    keywords = models.CharField(max_length=300)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title