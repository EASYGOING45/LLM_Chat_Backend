import abc
from typing import Dict, Tuple, Any

import requests
from bk_resource import BkApiResource
from django.conf import settings

from api.domains import KNOWLEDGE_BASE_URL


class KnowledgeBaseResource(BkApiResource, abc.ABC):
    """
    知识库 API基类
    """
    base_url = KNOWLEDGE_BASE_URL
    module_name = "knowledge"
    IS_STANDARD_FORMAT = False

    def build_header(self, validated_request_data: dict) -> Dict[str, str]:
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {settings.KNOWLEDGE_API_KEY}"}
        return headers


class ChatWithKnowledge(KnowledgeBaseResource):
    """
    知识库对话交互
    """
    action = "api/v1/chat/completions"
    method = "POST"


class GetKnowledgeList(KnowledgeBaseResource):
    """
    获取知识库列表
    """
    action = "api/core/dataset/list"
    method = "GET"
