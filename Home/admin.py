from django.contrib import admin
from Home.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = 'Blog'
admin.site.site_title = 'my prince'
admin.site.index_title = 'welcome to my blog'