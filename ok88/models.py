# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from ok88settings import *

class article(models.Model):
    article_id              = models.AutoField(primary_key=True)
    article_title           = models.CharField(max_length=DEFAULT_TITLE_LEN)
    article_content         = models.TextField()
    article_src             = models.CharField(max_length=DEFAULT_URL_LEN)
    article_add_time        = models.TimeField(null=True)
    article_thumbs          = models.TextField(null=True)