# -*- coding: utf-8 -*-

from bk_resource import Resource


class Demo(Resource):
    def perform_request(self, validated_request_data):
        return


class AccessKnowledgeBase(Resource):
    """
    访问知识库
    """

    def perform_request(self, validated_request_data):
        return validated_request_data
