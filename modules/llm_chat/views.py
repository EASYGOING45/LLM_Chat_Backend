# -*- coding: utf-8 -*-

from bk_resource import resource
from bk_resource.viewsets import ResourceRoute, ResourceViewSet


class LlmChatViewSet(ResourceViewSet):
    resource_routes = [
        # 查询模型实例详情
        ResourceRoute("GET", resource.llm_chat.get_model_info, endpoint="model_info"),
        # 查询可用模型列表
        ResourceRoute("GET", resource.llm_chat.get_running_models, endpoint="models_list"),
        # 模型对话交互
        ResourceRoute("POST", resource.llm_chat.chat_with_model, endpoint="chat"),
        # 三方交互
        ResourceRoute("POST", resource.llm_chat.chat_with_close_ai, endpoint="chat_third"),
        # 情感分析
        ResourceRoute("POST",resource.llm_chat.get_message_sentiment,endpoint="get_sentiment"),
    ]
