from django.contrib.sitemaps import Sitemap
from .models import Blog  # اطمینان حاصل کنید که مدل Blog به درستی import شده است

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.date  # یا هر متد دیگری که تاریخ آخرین تغییر را برمی‌گرداند