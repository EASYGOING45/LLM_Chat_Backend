# -*- coding: utf-8 -*-

from bk_resource import Resource
from django.utils.translation import gettext_lazy


class GetModelBaseInfo(Resource):
    name = gettext_lazy("获取模型基本信息")
    def perform_request(self, validated_request_data):
        return
