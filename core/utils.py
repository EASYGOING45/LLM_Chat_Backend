# -*- coding: utf-8 -*-
import json

from tencentcloud.common.common_client import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

import os
import csv
from django.conf import settings
from modules.knowledge.models import InterviewQuestion
from django.db import IntegrityError, DataError


def get_sentiment(text):
    """
    腾讯云-情感分析v2
    """
    try:
        cred = credential.Credential(settings.SECRET_ID, settings.SECRET_KEY)

        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # params = "{\"Text\":\"太棒了！\"}";
        # Prepare parameters
        params = json.dumps({"Text": text})
        common_client = CommonClient("nlp", "2019-04-08", cred, "", profile=clientProfile)
        response = common_client.call_json("AnalyzeSentiment", json.loads(params))
        print(response.get('Response').get('Sentiment'))
        return response.get('Response').get('Sentiment')

    except TencentCloudSDKException as err:
        print(err)


def import_csv_data():
    # 定义CSV文件所在的目录
    csv_dir = os.path.join(settings.BASE_DIR, 'data_process', 'cs_science', 'interview_questions', 'merged_csv_files')

    # 遍历目录中的所有CSV文件
    for filename in os.listdir(csv_dir):
        if filename.endswith('_combined.csv'):
            # 获取类别名称
            category = filename.replace('_combined.csv', '')

            # 打开CSV文件并读取内容
            file_path = os.path.join(csv_dir, filename)
            with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) < 2:
                        continue
                    question, answer = row[0], row[1]

                    # 尝试创建并保存InterviewQuestion实例
                    try:
                        InterviewQuestion.objects.create(
                            question=question,
                            answer=answer,
                            category=category
                        )
                    except (IntegrityError, DataError) as e:
                        print(f"Error inserting row: {row}. Error: {e}")
                        continue
            print(f'Successfully imported {filename}')

    print('All files have been imported successfully')

