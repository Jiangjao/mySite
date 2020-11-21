from django.db import models
from django import forms 
from captcha.fields import CaptchaField

# Create your models here.
class User(models.Model):
    gender = (
        ('male',"男"),
        ('female',"女"),
    )
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    sex = models.CharField( max_length=50,choices=gender,default="男")
    c_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    class Meta:
        # 元数据里定义用户按创建时间的反序排列，
        # 也就是最近的最先显示；
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.name + ":" + self.code

    class Meta:
         
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"


