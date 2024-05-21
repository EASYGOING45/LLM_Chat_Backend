# -*- coding: utf-8 -*-
import re

from django.utils.deprecation import MiddlewareMixin
import logging
from django.db.models import F

from modules.llm_chat.models import ApiRequestCount

logger = logging.getLogger(__name__)


class RecordUserBehaviorMiddleware(MiddlewareMixin):
    """
    自定义中间件-静默记录用户行为，进行数据埋点记录
    """

    def process_request(self, request):
        try:
            username = request.user.username
            # 使用正则表达式提取模块名称和详细接口
            match = re.match(r'/api/v\d+/(.+?)/(.+?)/', request.path)
            if match:
                module_name = match.group(1)
                api_name = match.group(2)
                logger.info(f"Module Name:{module_name}, API Name:{api_name}")
                api_request_count, _ = ApiRequestCount.objects.get_or_create(
                    api_category=module_name, api_name=api_name
                )
                api_request_count.request_count = F('request_count') + 1
                api_request_count.save()
        except Exception as e:
            logger.exception(f"Unexpected Exception occurs:{e}")
