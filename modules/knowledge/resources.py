# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy


class Demo(Resource):
    def perform_request(self, validated_request_data):
        return


class ChatWithKnowledge(Resource):
    """
    知识库对话交互
    """
    name = gettext_lazy('知识库对话交互')

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

    def perform_request(self, validated_request_data):
        return validated_request_data
