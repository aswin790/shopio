from django.db import models
from django.contrib.auth.models import User
# from django.db.models import Model

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 250)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
class item(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(category,on_delete = models.CASCADE, related_name = 'item')
    description = models.TextField(null = True, blank = True)
    price = models.FloatField()
    is_sold = models.BooleanField(default = False)
    location = models.CharField(max_length = 250,null =True,blank = True) #location of the product that you are selling
    year = models.IntegerField(null =True) #year of purchase
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'item')
    image = models.ImageField(upload_to ='item_images',blank=True,null=True)
    
    def __str__(self):
        return self.name




    

    
    
    
    
    
    
    
    
    



    


