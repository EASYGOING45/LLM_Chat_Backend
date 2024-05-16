# -*- coding: utf-8 -*-
from bk_resource import resource
from bk_resource.viewsets import ResourceViewSet, ResourceRoute


class CloseAiViewSet(ResourceViewSet):
    resource_routes = [
        # Close-AI交互
        ResourceRoute("POST", resource.close_ai.chat_with_close_ai, endpoint="chat_close"),
    ]
