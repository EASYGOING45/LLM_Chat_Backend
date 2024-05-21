# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.knowledge.serializers import ChatWithKnowledgeRequestSerializer, KnowledgeDetailRequestSerializer, \
    CollectionRequestSerializer


class GetKnowledgeList(Resource):
    """
    获取知识库列表
    """
    name = gettext_lazy("获取知识库列表")

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_knowledge_list()
        return data


class GetKnowledgeDetail(Resource):
    """
    查询知识库详情
    """
    name = gettext_lazy("查询知识库详情")
    RequestSerializer = KnowledgeDetailRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_knowledge_detail(
            knowledge_id=validated_request_data["knowledge_id"]
        )
        return data


class DeleteKnowledge(Resource):
    """
    删除知识库
    """
    name = gettext_lazy("删除知识库")
    RequestSerializer = KnowledgeDetailRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.delete_knowledge(
            knowledge_id=validated_request_data["knowledge_id"]
        )
        return data


class GetCollectionList(Resource):
    """
    查询知识库下的集合列表
    """
    name = gettext_lazy("查询知识库下的集合列表")
    RequestSerializer = CollectionRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_collection_list(
            pageNum=1,
            pageSize=10,
            datasetId=validated_request_data.get("dataset_id"),
            parentId=None,
            searchText=""
        )
        return data


class ChatWithKnowledge(Resource):
    """
    知识库对话交互
    """
    name = gettext_lazy('知识库对话交互')
    RequestSerializer = ChatWithKnowledgeRequestSerializer

    def perform_request(self, validated_request_data):
        chat_id = validated_request_data.get('chatId')
        messages = validated_request_data.get('messages')
        data = api.knowledge.chat_with_knowledge(
            chatId=chat_id,
            stream='false',
            detail='false',
            messages=messages
        )
        return data


class AccessKnowledgeBase(Resource):
    """
    访问知识库
    """
    name = gettext_lazy("访问知识库")

    def perform_request(self, validated_request_data):
        return validated_request_data
