# -*- coding: utf-8 -*-

from bk_resource import Resource, api
from django.utils.translation import gettext_lazy

from modules.knowledge.serializers import ChatWithKnowledgeRequestSerializer, KnowledgeDetailRequestSerializer, \
    CollectionRequestSerializer, KnowledgeIdRequestSerializer, ItemRequestSerializer, KnowledgeSearchRequestSerializer


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
    RequestSerializer = KnowledgeIdRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_collection_list(
            pageNum=1,
            pageSize=10,
            datasetId=validated_request_data.get("dataset_id"),
            parentId=None,
            searchText=""
        )
        return data


class GetCollectionDetail(Resource):
    """
    查询知识库下集合详情
    """
    name = gettext_lazy("查询知识库下集合详情")
    RequestSerializer = CollectionRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_collection_detail(
            collection_id=validated_request_data["collection_id"],
        )
        return data


class DeleteCollection(Resource):
    """
    删除知识库下的一个集合
    """
    name = gettext_lazy("删除知识库下的一个集合")
    RequestSerializer = CollectionRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.delete_collection(
            collection_id=validated_request_data["collection_id"]
        )
        return data


class GetItemList(Resource):
    """
    查询知识条目列表
    """
    name = gettext_lazy("查询知识条目列表")
    RequestSerializer = CollectionRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_data_item_list(
            pageNum=1,
            pageSize=10,
            collectionId=validated_request_data["collection_id"],
            searchText=""
        )
        return data


class GetItemDetail(Resource):
    """
    查询知识条目详情
    """
    name = gettext_lazy("查询知识条目详情")
    RequestSerializer = ItemRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.get_item_detail(
            item_id=validated_request_data["item_id"],
        )
        return data


class DeleteItem(Resource):
    """
    删除知识条目
    """
    name = gettext_lazy("删除知识条目")
    RequestSerializer = ItemRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.delete_item(
            item_id=validated_request_data["item_id"],
        )
        return data


class SearchKnowledge(Resource):
    """
    知识库对话搜索交互
    """
    name = gettext_lazy("知识库对话搜索交互")
    RequestSerializer = KnowledgeSearchRequestSerializer

    def perform_request(self, validated_request_data):
        data = api.knowledge.search_knowledge(
            datasetId=validated_request_data["dataset_id"],
            text=validated_request_data["text"],
            limit=5000,
            similarity=0,
            searchMode="embedding",
            usingReRank=False
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
