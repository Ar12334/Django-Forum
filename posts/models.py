from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank = False, null = False, max_length=14, db_index= True, default = 'Anonymous'
    )
    body = models.CharField(
        'Body' , blank= True, null= True, max_length=140, db_index= True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True , auto_now_add= True
    )