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
    ]
