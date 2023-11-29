from django.db import models
from django.contrib.auth.models import User


# Model for Post and Comment 

class Post(model.Models):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default="placeholder", blank=False)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name = 'likes', blank=True)
    slug = models.SlugField(unique=True)
    approved = models.BooleanField(default=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse ('post_detail', args=[str(self.slug)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    body = models.TextField()
    approved = models.BooleanField(default=False)



