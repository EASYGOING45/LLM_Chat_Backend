import logging
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

    Cplus_questions = InterviewQuestion.objects.filter(category="C++").count()
    Golang_questions = InterviewQuestion.objects.filter(category="Golang").count()
    HTML_questions = InterviewQuestion.objects.filter(category="HTML").count()
    JAVA_questions = InterviewQuestion.objects.filter(category="Java").count()
    Vue_questions = InterviewQuestion.objects.filter(category="Vue").count()
    Spring_questions = InterviewQuestion.objects.filter(category="Spring").count()
    Python_questions = InterviewQuestion.objects.filter(category="Python").count()
    Linux_questions = InterviewQuestion.objects.filter(category="Linux").count()
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
                    "C++_questions": Cplus_questions,
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
