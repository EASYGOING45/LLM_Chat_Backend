# -*- coding: utf-8 -*-

from django.urls import include, path

urlpatterns = [
    path("", include("modules.llm_chat.urls")),
    path("", include("modules.user_manage.urls")),
    path("", include("modules.closeai.urls")),
    path("", include("modules.knowledge.urls")),
]
