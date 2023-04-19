from datetime import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):       
        return  [
            'home',
            'company:introduction',
            'company:history',
            'company:mainbusiness',
            'company:organizationchart',
            'company:map',
            'company:revenue',
            
            'inquiry:inquiry',
            'inquiry:success',
            
            'notice:bulletin_board',
            
            'product:product_goal',
            'product:parts',
            'product:download_sample',
            'product:facility_list',
            'product:press',  
            
        ]

    def location(self, item):
        return reverse(item)
    
    def lastmod(self, item):
        if item == 'home':
            return datetime.now()
        else:
            return datetime(2023, 4, 19)  # replace with the actual last modification date for each page
