from django.contrib import admin
from django.utils.translation import gettext_lazy as _

site = admin.site

site.site_title  = _('Artists admin')
site.site_header = _('Artists administration')
site.index_title = _('Site administration')
