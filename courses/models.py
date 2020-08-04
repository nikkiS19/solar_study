from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title=models.CharField(max_length=100)
    addlesson=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
