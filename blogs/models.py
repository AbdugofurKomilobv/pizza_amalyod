from django.db import models
from django.contrib.auth import get_user_model

from common.models import BaseModel

UserModel = get_user_model()


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog category"
        verbose_name_plural = "Blog categories"


class BlogTagModel(models.Model):
    title = models.CharField(max_length=128)


  


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog tag"
        verbose_name_plural = "Blog tags"

class BlogModel(BaseModel):
    title = models.CharField(max_length=128)
    img1 = models.ImageField(upload_to='blogs')
    img2 = models.ImageField(upload_to="blogs")
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()


    ctegories = models.ManyToManyField(BlogCategoryModel,related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel,related_name='blogs')





    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog category"
        verbose_name_plural = "Blog categories"

class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_comments')
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE, related_name='comments')
    


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog comment"
        verbose_name_plural = "Blog comments"


class BlogLikeModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='like_comments')
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE, related_name='likes')
    




    def __str__(self):
        return f'{self.user.get_full_name()} liked to  {self.blog.title}'


    class Meta:
        verbose_name = "Blog like"
        verbose_name_plural = "Blog likes"


class BlogKatalogModel(BaseModel):
    title = models.CharField(max_length=128)
    status = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog katalog'
        verbose_name_plural = 'Blog kataloglar'

class BlogMaxsulotModel(BaseModel):
    name = models.CharField(max_length=128)
    narx = models.IntegerField(verbose_name='Blog katalog')

    kategorya = models.ForeignKey(BlogKatalogModel,on_delete=models.CASCADE,related_name='maxsulotlar')
    ombor = models.BooleanField(default=True, verbose_name='omborda mavjud')


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Blog maxsulot'
        verbose_name_plural = 'Blog maxsulotlar'
