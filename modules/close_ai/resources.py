# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.close_ai.serializers import ChatWithModelRequestSerializer


class ChatWithCloseAi(Resource):
    """
    CLose-AI 模型对话交互
    """
    name = gettext_lazy("CloseAI模型交互")
    RequestSerializer = ChatWithModelRequestSerializer

    def perform_request(self, validated_request_data):
        model = validated_request_data.get('model')
        messages = validated_request_data.get("messages")
        data = api.close_ai.chat_with_completions(model=model, messages=messages)
        return data
