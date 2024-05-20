# -*- coding: utf-8 -*-
from bk_resource import resource
from bk_resource.viewsets import ResourceViewSet, ResourceRoute


class KnowledgeViewSet(ResourceViewSet):
    resource_routes = [
        ResourceRoute('GET', resource.knowledge.access_knowledge_base, endpoint='knowledge_base'),
    ]
