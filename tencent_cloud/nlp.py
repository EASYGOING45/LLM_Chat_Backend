# -*- coding: utf-8 -*-
import json

from tencentcloud.common.common_client import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    cred = credential.Credential("AKIDcCczGew6HMGcCeB3DX5b1JUkz7JSQH2V", "jboEsU1kPwNe9bv32uaASmGi5c5Uo7Ws")

    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    # params = "{\"Text\":\"太棒了！\"}";
    params = "{\"Text\": \"这个商品太坏了！\"}"
    common_client = CommonClient("nlp", "2019-04-08", cred, "", profile=clientProfile)
    response = common_client.call_json("AnalyzeSentiment", json.loads(params))
    print(response.get('Response').get('Sentiment'))

except TencentCloudSDKException as err:
    print(err)
