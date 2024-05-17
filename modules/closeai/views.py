# -*- coding: utf-8 -*-
from bk_resource import resource
from bk_resource.viewsets import ResourceViewSet, ResourceRoute


class CloseaiViewSet(ResourceViewSet):
    resource_routes = [
        # 查询模型实例详情
        ResourceRoute("GET", resource.closeai.demo, endpoint="demo"),
    ]
