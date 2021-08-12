from django.db import models

# Create your models here.
class Letter(models.Model):   # Letter라는 이름의 클래스
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):  # title이 뜨게 해줌
        return self.title