from django.contrib import admin
# from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy

site = admin.site

site.site_title = gettext_lazy('My site admin')
site.site_header = gettext_lazy('My administration')
site.index_title = gettext_lazy('Site administration')
