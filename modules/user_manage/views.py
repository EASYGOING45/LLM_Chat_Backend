# -*- coding: utf-8 -*-
from bk_resource import resource
from bk_resource.viewsets import ResourceRoute, ResourceViewSet


class UserManageViewSet(ResourceViewSet):
    resource_routes = [
        # 查询用户列表
        ResourceRoute("GET", resource.user_manage.get_users, endpoint="users_list"),
        # 更新用户信息
        ResourceRoute("GET", resource.user_manage.update_user, endpoint="update_user"),
    ]
