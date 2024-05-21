# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy
from rest_framework import serializers


class MessageArraySerializer(serializers.Serializer):
    """
    对话历史上下文序列化器
    """

    role = serializers.CharField(required=True, label=gettext_lazy("角色"))
    content = serializers.CharField(required=True, label=gettext_lazy("内容"))


class ChatWithKnowledgeRequestSerializer(serializers.Serializer):
    """
    模型交互对话-请求序列化器
    """

    messages = MessageArraySerializer(many=True, required=True, label=gettext_lazy("历史上下文消息"))
    chat_id = serializers.CharField(required=True, label=gettext_lazy("对话UID"))


class KnowledgeDetailRequestSerializer(serializers.Serializer):
    """
    查询知识库详情-请求序列化器
    """
    knowledge_id = serializers.CharField(required=True, label=gettext_lazy("知识库ID"))


class CollectionRequestSerializer(serializers.Serializer):
    """
    集合相关CRUD接口-请求序列化器
    """
    dataset_id = serializers.CharField(required=True, label=gettext_lazy("数据库ID"))
