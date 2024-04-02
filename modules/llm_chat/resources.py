# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.llm_chat.serializers import GetModelInfoRequestSerializer


class GetModelInfo(Resource):
    """
    查询模型详情信息
    """

    name = gettext_lazy("查询模型详情信息")
    RequestSerializer = GetModelInfoRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.xinference.get_model_info(model_uid=validated_request_data.get("model_uid"))
        # data = api.xinference.get_status()
        return data
