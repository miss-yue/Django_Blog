# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article.models import Article

# Register your models here.
admin.site.register(Article) # 将 Article 注入 admin 后台管理