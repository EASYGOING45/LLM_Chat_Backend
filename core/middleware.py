# -*- coding: utf-8 -*-
import re

from django.utils.deprecation import MiddlewareMixin
import logging
from django.db.models import F

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
        except Exception as e:
            logger.exception(f"Unexpected Exception occurs:{e}")
