# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.llm_chat.serializers import (
    ChatWithModelRequestSerializer,
    GetModelInfoRequestSerializer,
)

# TODO：日志&异常处理&序列化器补足&单元测试 0408


class GetModelInfo(Resource):
    """
    查询模型详情信息
    """

    name = gettext_lazy("查询模型详情信息")
    RequestSerializer = GetModelInfoRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.xinference.get_model_info(model_uid=validated_request_data.get("model_uid"))
        return data


class GetRunningModels(Resource):
    """
    查询可用模型
    """

    name = gettext_lazy("查询可用模型")
    RequestSerializer = None

    def perform_request(self, validated_request_data):
        data = api.xinference.get_models_list()
        return data


class ChatWithModel(Resource):
    """
    模型对话交互
    """

    name = gettext_lazy("模型对话交互")
    RequestSerializer = ChatWithModelRequestSerializer

    def perform_request(self, validated_request_data):
        messages = validated_request_data.get("messages")  # 对话上下文 PROMPT
        model = validated_request_data.get("model")  # 对话目标模型
        data = api.xinference.chat_with_model(messages=messages, model=model)
        return data
