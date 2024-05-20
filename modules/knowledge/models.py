# -*- coding: utf-8 -*-

from django.db import models


class InterviewQuestion(models.Model):
    question = models.TextField(verbose_name="问题")
    answer = models.TextField(verbose_name="回答")
    category = models.CharField(max_length=100, verbose_name="所属分类")

    def __str__(self):
        return self.question[:50]  # 返回问题的前50个字符作为字符串表示

    class Meta:
        verbose_name = "面试题"
        verbose_name_plural = "面试题"
