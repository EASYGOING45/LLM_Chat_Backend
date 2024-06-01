import logging

from celery.schedules import crontab
from celery.task import periodic_task
from django.conf import settings

# 获取或创建一个logger
logger = logging.getLogger(__name__)

@periodic_task(run_every=crontab())
def report_custom_monitor_metrics():
    """
    上报自定义监控指标
    """
    logger.info("进行自定义指标上报")

    active_tasks = TaskResult.objects.filter(status="STARTED").count()
    failed_tasks = TaskResult.objects.filter(status="FAILURE").count()
    success_tasks = TaskResult.objects.filter(status="SUCCESS").count()
    backup_task_count = MonitorMetrics.objects.first().backup_tasks_counter

    timestamp = int(time.time() * MILLISECONDS_IN_SECOND)
    proxy_url = settings.APM_METRIC_PUSH_URL
    request_json = {
        "data_id": int(settings.APM_METRIC_ID),
        # 数据通道标识验证码，必需项
        "access_token": settings.APM_METRIC_TOKEN,
        "data": [
            {
                "metrics": {
                    "active_tasks": active_tasks,
                    "failed_tasks": failed_tasks,
                    "success_tasks": success_tasks,
                    "backup_tasks_count": backup_task_count,
                },
                "target": extract_ip(),
                "dimension": {"module": "db", "location": "guangdong"},
                "timestamp": timestamp,
            }
        ],
    }
    logger.info("自定义指标上报完成")
    try:
        response = requests.post(proxy_url, json=request_json)
        response_text = response.text
        logger.info(f"自定义指标上报成功，响应：{response_text}")
    except RequestException as e:
        response_text = str(e)
        logger.error(f"自定义指标上报失败，响应：{response_text}", exc_info=True)