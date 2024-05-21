# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy


class ApiRequestCount(models.Model):
    """
    API请求次数记录Model，用于运营分析
    """
    api_category = models.CharField(verbose_name=gettext_lazy("API类别"), max_length=255)
    api_name = models.CharField(verbose_name=gettext_lazy("API名称"), max_length=255)
    request_count = models.IntegerField(verbose_name="请求次数", default=0)

    class Meta:
        unique_together = ("api_name", "api_category")  # 联合唯一索引
        verbose_name = gettext_lazy("API请求次数")
        verbose_name_plural = gettext_lazy("API请求次数")

    def __str__(self):
        return f"{self.api_name} - {self.request_count}"