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


class GetKnowledgeDetail(KnowledgeBaseResource):
    """
    查询知识库详情
    """
    action = "/api/core/dataset/detail?id={knowledge_id}"
    method = "GET"
    url_keys = ["knowledge_id"]


class DeleteKnowledge(KnowledgeBaseResource):
    """
    删除一个知识库，不允许批量删除
    """
    action = "/api/core/dataset/delete?id={knowledge_id}"
    method = "GET"
    url_keys = ["knowledge_id"]


class GetCollectionList(KnowledgeBaseResource):
    """
    查询知识库下集合列表
    """
    action = "/api/core/dataset/collection/list"
    method = "POST"


class GetCollectionDetail(KnowledgeBaseResource):
    """
    查询知识库下集合详情
    """
    action = "/api/core/dataset/collection/detail?id={collection_id}"
    method = "GET"
    url_keys = ["collection_id"]


class DeleteCollection(KnowledgeBaseResource):
    """
    删除知识库下的一个集合
    """
    action = "/api/core/dataset/collection/delete?id={collection_id}"
    method = "GET"
    url_keys = ["collection_id"]

