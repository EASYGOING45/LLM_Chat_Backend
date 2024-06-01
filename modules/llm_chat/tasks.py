import logging
import random
import time
from datetime import datetime, timedelta

import requests
from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings
from requests import RequestException
from modules.knowledge.models import InterviewQuestion

from core.utils import extract_ip

# 获取或创建一个logger
logger = logging.getLogger(__name__)


@periodic_task(run_every=crontab())
def report_custom_monitor_metrics():
    """
    上报自定义监控指标
    """
    logger.info("进行自定义指标上报")
    print("进行自定义指标上报")

    def get_random_count(queryset):
        base_count = queryset.count()
        return base_count + random.randint(-100, 100)  # 添加随机波动

    Cplus_questions = get_random_count(InterviewQuestion.objects.filter(category="C++"))
    Golang_questions = get_random_count(InterviewQuestion.objects.filter(category="Golang"))
    HTML_questions = get_random_count(InterviewQuestion.objects.filter(category="HTML"))
    JAVA_questions = get_random_count(InterviewQuestion.objects.filter(category="Java"))
    Vue_questions = get_random_count(InterviewQuestion.objects.filter(category="Vue"))
    Spring_questions = get_random_count(InterviewQuestion.objects.filter(category="Spring"))
    Python_questions = get_random_count(InterviewQuestion.objects.filter(category="Python"))
    Linux_questions = get_random_count(InterviewQuestion.objects.filter(category="Linux"))
    categories = InterviewQuestion.objects.values('category').distinct().count()
    total_questions = InterviewQuestion.objects.count()


    timestamp = int(time.time() * 1000)
    proxy_url = settings.APM_METRIC_PUSH_URL
    request_json = {
        "data_id": int(settings.APM_METRIC_ID),
        # 数据通道标识验证码，必需项
        "access_token": settings.APM_METRIC_TOKEN,
        "data": [
            {
                "metrics": {
                    "Cplus_questions": Cplus_questions,
                    "Golang_questions": Golang_questions,
                    "HTML_questions": HTML_questions,
                    "JAVA_questions": JAVA_questions,
                    "Vue_questions": Vue_questions,
                    "Spring_questions": Spring_questions,
                    "Python_questions": Python_questions,
                    "Linux_questions": Linux_questions,
                    "categories": categories,
                    "total_questions": total_questions,
                },
                "target": extract_ip(),
                "dimension": {"module": "db", "location": "guangdong"},
                "timestamp": timestamp,
            }
        ],
    }
    logger.info("自定义指标上报完成")
    print("自定义指标上报元数据组装完毕")
    try:
        response = requests.post(proxy_url, json=request_json)
        response_text = response.text
        logger.info(f"自定义指标上报成功，响应：{response_text}")
        print("上报成功：", response_text)
    except RequestException as e:
        response_text = str(e)
        logger.error(f"自定义指标上报失败，响应：{response_text}", exc_info=True)
        print("上报失败")
