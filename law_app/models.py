from statistics import mode
from django.db import models

class Generation(models.Model):
    generation = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="授業タイトル")
    body = models.TextField()

class Fields(models.Model):
    field_name = models.CharField(max_length=255, verbose_name="分野の名前", primary_key=True)
    body = models.TextField()

class Qformat(models.Model):
    format_id = models.IntegerField(primary_key=True)
    format_name = models.CharField(max_length=255, verbose_name="問題の種類")

class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    fields = models.ForeignKey(Fields, on_delete=models.CASCADE)
    q_format = models.ForeignKey(Qformat, on_delete=models.CASCADE)
    slug = models.SlugField(blank=False,unique=True)
    question = models.TextField()
    answer = models.TextField()
    explanation = models.TextField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)

class Answers(models.Model):
    number = models.IntegerField(primary_key=True, auto_created=True)
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField()
    trueORfalse = models.IntegerField()
    posted_data = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, verbose_name="お問い合わせ内容")
    body = models.TextField(verbose_name="具体的に")