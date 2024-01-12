from django.db import models
from django.contrib.auth.models import User
from item.models import item
# Create your models here.


class conversation(models.Model):
    item = models.ForeignKey(item,related_name = 'conversation',on_delete = models.CASCADE)
    members = models.ManyToManyField(User,related_name='conversation')
    created_at = models.DateTimeField(auto_now_add = True)
    modefied_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-modefied_at',)


class conversationMessage(models.Model):
    conversation = models.ForeignKey(conversation,on_delete = models.CASCADE,related_name = 'message')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User,related_name = 'created_message',on_delete = models.CASCADE)
    



