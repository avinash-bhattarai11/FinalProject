from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    title =models.CharField(max_length=255)
    pub_date =models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
    

class Comment(models.Model):
    post =models.ForeignKey(Product,related_name='comments',on_delete=CASCADE)
    name =models.CharField(max_length=255)
    body =models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    remark =models.CharField(max_length=225)
    
   

    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)