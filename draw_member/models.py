from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	location = models.CharField(max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)
    
    # set title is unicode
    def __unicode__(self)
        return self.title
        
class Sell_product(models.Model)
    pname = models.CharField(max_length=100)
    pprice = models.DecimalField(max_digit=3, decimal_places=0)
    pdetail = models.TextField(max_length=200)
    post = models.ForeignKey(Post)
    
    # set pname is unicode
    def __unicode__(self)
        return self.pname