from django.db import models
from datetime import datetime

# Create your models here.
class Static_Page(models.Model):

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    name = models.CharField(max_length=254, default='')
    url = models.CharField(max_length=254, default='', unique=True)
    title = models.CharField(max_length=254, default='', null=True)
    header = models.CharField(max_length=254, default='', null=True, blank=True)
    content = models.TextField()
    YESNOCHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    published = models.CharField(max_length=3, default='No', choices=YESNOCHOICES)
    onmenu = models.CharField(max_length=3, default='No',  choices=YESNOCHOICES)
    order = models.IntegerField(default=0)
    created_date = models.DateField(default=datetime.now)
    updated_date = models.DateField(default=datetime.now)


    def __str__(self):
        return self.name