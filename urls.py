# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from core.permissions import SwaggerPermission

info = openapi.Info(
    title="llm-chat",
    default_version="v1",
    description="llm-chat",
)
schema_view = get_schema_view(
    info,
    public=True,
    permission_classes=(SwaggerPermission,),
)


def get_status(request):
    from bk_resource import api

    return api.xinference.get_status()


urlpatterns = [
    # 出于安全考虑，默认屏蔽admin访问路径。
    # 开启前请修改路径随机内容，降低被猜测命中几率，提升安全性
    path("bkadmin/", admin.site.urls),
    path("account/", include("blueapps.account.urls")),
    path("swagger/", schema_view.with_ui(cache_timeout=0), name="schema-swagger-ui"),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/v1/", include("modules.urls")),
    path("status/", get_status),
]

for _module in settings.DEPLOY_MODULE:
    urlpatterns.append(path(f"{_module}/", include(f"{settings.MODULE_PATH}.{_module}.urls")))
