from django.db import models

# Create your models here.

class Genre(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=300,null=True)

    def __str__(self):
        return '{} {}'.format(self.name,self.description)

class Movie(models.Model):
    title=models.CharField(max_length=100)
    release_date=models.DateField()
    duration=models.PositiveIntegerField()
    summary=models.TextField(max_length=300)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.title,self. release_date,self. duration,self.summary,self.genre)





