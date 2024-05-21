# -*- coding: utf-8 -*-

from bk_resource import Resource
from blueapps.account.models import User

# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy

from modules.user_manage.serializers import UpdateUserRequestSerializer


class GetUsers(Resource):
    """
    获取用户信息（account_user)
    """

    name = gettext_lazy("获取用户信息")
    RequestSerializer = None

    def perform_request(self, validated_request_data):
        users = User.objects.all()
        users_data = []
        for user in users:
            users_data.append(
                {
                    "username": user.username,
                    "is_staff": user.is_staff,
                    "is_active": user.is_active,
                    "is_superuser": user.is_superuser,
                }
            )
        return users_data


class UpdateUser(Resource):
    """
    更新用户信息
    """

    name = gettext_lazy("更新用户信息")
    RequestSerializer = UpdateUserRequestSerializer

    def perform_request(self, validated_request_data):
        username = validated_request_data["username"]
        user = User.objects.get(username=username)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return {
            "username": user.username,
            "is_staff": user.is_staff,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
        }


class UserLogin(Resource):
    """
    用戶登錄
    """
    name = gettext_lazy("用戶登錄")

    def perform_request(self, validated_request_data):
        users = User.objects.all()
        users_data = []
        for user in users:
            users_data.append(
                {
                    "username": user.username,
                    "is_staff": user.is_staff,
                    "is_active": user.is_active,
                    "is_superuser": user.is_superuser,
                }
            )
        return users_data
