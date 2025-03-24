from django.db import models
import jdatetime

class SiteInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام سایت")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to='logo/%Y/%m/%d', blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="شماره تلفن")
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name="ایمیل")


    x = models.URLField(blank=True, null=True, verbose_name="لینک ایکس")
    instagram = models.URLField(blank=True, null=True, verbose_name="لینک اینستاگرام")
    linkedin = models.URLField(blank=True, null=True, verbose_name="لینک لینکدین")
    youtube = models.URLField(blank=True, null=True, verbose_name="لینک یوتیوب")
    github = models.URLField(blank=True, null=True, verbose_name="لینک گیت هاب")


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین بروزرسانی')

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @classmethod
    def get_info(cls):
        return cls.objects.first()  

    
    def get_persian_date(self):
        # تبدیل تاریخ میلادی به تاریخ شمسی
        persian_date = jdatetime.datetime.fromgregorian(datetime=self.created_at)
        return persian_date.strftime('%Y/%m/%d')       