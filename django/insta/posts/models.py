from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(instance,filename):
    # return 'posts/{}/{}'.format(instance.content,filename)
    return f'posts/{instance.content}/{filename}'
    # return f'posts/{instance.content}/{instance.content}.jpg'
    # return f 'posts/images/{filename}'
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.TextField()
    # image=models.ImageField(blank=True)
    image=ProcessedImageField(
                    upload_to='posts/images', #저장위치
                    processors=[ResizeToFill(600,600)], #처리할 작업 목록
                    format='JPEG', #저장포멧
                    options={'quality':90}, #옵션
                )
                
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')
    
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
    
    