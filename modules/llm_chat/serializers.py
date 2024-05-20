# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy
from rest_framework import serializers


class GetModelInfoRequestSerializer(serializers.Serializer):
    """
    查询模型基本信息-请求序列化器
    """

    model_uid = serializers.CharField(required=True, label=gettext_lazy("模型UID"))


class HistoryMessageSerializer(serializers.Serializer):
    """
    对话历史上下文序列化器
    """

    role = serializers.CharField(required=True, label=gettext_lazy("角色"))
    content = serializers.CharField(required=True, label=gettext_lazy("内容"))


class ChatWithModelRequestSerializer(serializers.Serializer):
    """
    模型交互对话-请求序列化器
    """

    messages = HistoryMessageSerializer(many=True, required=True, label=gettext_lazy("历史上下文消息"))
    model = serializers.CharField(required=True, label=gettext_lazy("模型UID"))


class ChatWithThirdPartyRequestSerializer(serializers.Serializer):
    """
    模型交互对话-请求序列化器
    """

    messages = HistoryMessageSerializer(many=True, required=True, label=gettext_lazy("历史上下文消息"))
