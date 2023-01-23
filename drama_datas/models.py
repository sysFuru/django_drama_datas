from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    name = models.CharField('会社名', max_length=128)
    country = models.CharField('国名', max_length=128, blank=True)
    memo = models.TextField('メモ', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.name

# class LeadRole(models.Model):
    
class Actor(models.Model):
    name = models.CharField('氏名', max_length=128)
    country = models.CharField('出身地', max_length=128, blank=True)
    #sex = models.IntegerField('性別',blank=True)
    SEX = ((1,'男'),(2,'女'),(3,'その他'))
    sex = models.IntegerField('性別',default=1,choices=SEX,blank=True)
    birthday = models.DateField('生年月日',null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("更新日", auto_now=True, null=True)

    def __str__(self):
        return self.name

class DramaData(models.Model):
    title = models.CharField('タイトル', max_length=128)
    year = models.IntegerField('放送年', default=2021)
    PATERN = ((1,'連続'),(2,'単発'))
    patern = models.IntegerField('区分',default=1,choices=PATERN,blank=True)
    company = models.ForeignKey(
        Company,
        verbose_name="制作会社",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    memo = models.TextField('メモ', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("更新日", auto_now=True, null=True)

    def __str__(self):
        return self.title

class Cast(models.Model):
    title = models.ForeignKey(
        DramaData,
        verbose_name="出演作",
        on_delete=models.CASCADE
    )
    name = models.ForeignKey(
        Actor,
        verbose_name="氏名",
        on_delete=models.CASCADE
    )
    ROLE = ((1,"主演"),(2,"レギュラー"),(3,"友情出演"),(4,"特別出演"),(5,"ゲスト出演"),(6,"カメオ出演"))
    role = models.IntegerField("役区分", default=1, choices=ROLE)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("更新日", auto_now=True, null=True)

    def __str__(self):
        return self.name.name+"("+self.title.title+")"