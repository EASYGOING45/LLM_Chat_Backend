# -*- coding: utf-8 -*-

import abc

import requests
from bk_resource import BkApiResource
from bk_resource.exceptions import APIRequestError
from bk_resource.utils.logger import logger
from django.utils.encoding import force_str
from django.utils.translation import gettext
from requests.exceptions import HTTPError

from api.domains import XINFERENCE_URL


class LLMBaseResource(BkApiResource, abc.ABC):
    """
    Xinference API基类
    """

    base_url = XINFERENCE_URL
    module_name = "xinference"

    def parse_response(self, response: requests.Response) -> any:
        """
        在提供数据给response_serializer之前，对数据作最后的处理，子类可进行重写
        """
        try:
            result_json = response.json()
        except Exception as err:
            logger.exception("{} => {}".format(gettext("Response Parse Error"), err))
            result_json = response.content

        try:
            response.raise_for_status()
        except HTTPError as err:
            logger.exception(gettext("【%s】请求API错误：%s，url: %s ") % (self.module_name, err, response.request.url))
            content = str(err.response.content)
            if isinstance(result_json, dict):
                content = "[{code}] {message}".format(code=result_json.get("code"), message=result_json.get("message"))
            raise APIRequestError(
                module_name=self.module_name,
                url=self.action,
                status_code=response.status_code,
                result=content,
            )

        if not self.IS_STANDARD_FORMAT:
            return result_json

        if not isinstance(result_json, dict):
            raise APIRequestError(
                module_name=self.module_name,
                url=self.action,
                result=gettext("返回格式有误 => %s") % force_str(result_json),
            )

        if not result_json.get("result", True) and result_json.get("code") != 0:
            msg = result_json.get("message", "")
            request_id = result_json.pop("request_id", "") or response.headers.get("x-bkapi-request-id", "")
            logger.error(
                "【Module: %s】【Action: %s】(%s) get error：%s",
                self.module_name,
                self.action,
                request_id,
                msg,
                extra=dict(module_name=self.module_name, url=response.request.url),
            )
            raise APIRequestError(
                module_name=self.module_name,
                url=self.action,
                result=result_json,
            )
        return result_json


class GetStatus(LLMBaseResource):
    """
    查看服务器当前状态
    """

    action = "/status"
    method = "GET"


class GetClusterInfo(LLMBaseResource):
    """
    查看集群设备信息
    """

    action = "/v1/cluster/info"
    method = "GET"


class GetClusterVersion(LLMBaseResource):
    """
    查看集群框架版本信息
    """

    action = "v1/cluster/version"
    method = "GET"


class GetModelInstances(LLMBaseResource):
    """
    查看模型实例
    可选参数：model_name 模型名称
            model_uid 模型id
    """

    action = "v1/models/instances"
    method = "GET"


class GetModelsList(LLMBaseResource):
    """
    查看模型列表
    返回模型列表、模型描述信息等
    """

    action = "v1/models"
    method = "GET"


class GetModelInfo(LLMBaseResource):
    """
    查看模型信息
    """

    action = "v1/models/{model_uid}"
    method = "GET"
    url_keys = ["model_uid"]
