import abc
from typing import Dict, Tuple, Any

import requests
from bk_resource import BkApiResource
from django.conf import settings

from api.domains import CLOSE_AI_URL


class CloseAiBaseResource(BkApiResource, abc.ABC):
    """
    Close AI  API基类
    """
    base_url = CLOSE_AI_URL
    module_name = "close"
    IS_STANDARD_FORMAT = False

    def build_header(self, validated_request_data: dict) -> Dict[str, str]:
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {settings.CLOSE_API_KEY}"}
        return headers


class ChatWithCompletions(CloseAiBaseResource):
    """
    模型交互对话
    """
    action = "v1/chat/completions"
    method = "POST"

