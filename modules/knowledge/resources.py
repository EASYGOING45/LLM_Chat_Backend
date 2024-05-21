# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.knowledge.serializers import ChatWithKnowledgeRequestSerializer, KnowledgeDetailRequestSerializer


class GetKnowledgeList(Resource):
    """
    获取知识库列表
    """
    name = gettext_lazy("获取知识库列表")

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_knowledge_list()
        return data


class GetKnowledgeDetail(Resource):
    """
    查询知识库详情
    """
    name = gettext_lazy("查询知识库详情")
    RequestSerializer = KnowledgeDetailRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_knowledge_detail(
            knowledge_id=validated_request_data["knowledge_id"]
        )
        return data


class ChatWithKnowledge(Resource):
    """
    知识库对话交互
    """
    name = gettext_lazy('知识库对话交互')
    RequestSerializer = ChatWithKnowledgeRequestSerializer

    def perform_request(self, validated_request_data):
        chat_id = validated_request_data.get('chatId')
        messages = validated_request_data.get('messages')
        data = api.knowledge.chat_with_knowledge(
            chatId=chat_id,
            stream='false',
            detail='false',
            messages=messages
        )
        return data


class AccessKnowledgeBase(Resource):
    """
    访问知识库
    """
    name = gettext_lazy("访问知识库")

    def perform_request(self, validated_request_data):
        return validated_request_data
