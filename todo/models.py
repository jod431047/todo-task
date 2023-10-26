from django.db import models

# Create your models here.

TODO_STATUS =(
    ('notstarted','notstarted'),
    ('inprogress','inprogress'),
    ('completed','completed'),
    
)

class Todo(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=20,choices=TODO_STATUS,default='notstarted')
    
    def __str__(self):
        return self.name
    
    
    