# -*- coding: utf-8 -*-
from bk_resource import resource
from bk_resource.viewsets import ResourceViewSet, ResourceRoute


class KnowledgeViewSet(ResourceViewSet):
    resource_routes = [
        # 访问知识库
        ResourceRoute('GET', resource.knowledge.access_knowledge_base, endpoint='knowledge_base'),
        # 知识库对话交互
        ResourceRoute("POST", resource.knowledge.chat_with_knowledge, endpoint='chat_with_knowledge'),
        # 获取知识库列表
        ResourceRoute("GET", resource.knowledge.get_knowledge_list, endpoint='knowledge_list'),
        # 查询知识库详情
        ResourceRoute("GET", resource.knowledge.get_knowledge_detail, endpoint='knowledge_detail'),
        # 删除知识库
        ResourceRoute("GET", resource.knowledge.delete_knowledge, endpoint='delete_knowledge'),
        # 查询知识库下集合列表
        ResourceRoute("POST", resource.knowledge.get_collection_list, endpoint='collection_list'),
        # 查询集合详情
        ResourceRoute("GET",resource.knowledge.get_collection_detail, endpoint='collection_detail'),
    ]
