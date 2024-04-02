# -*- coding: utf-8 -*-
from django.utils.translation import gettext_lazy
from rest_framework import serializers


class GetModelInfoRequestSerializer(serializers.Serializer):
    model_uid = serializers.CharField(required=True, label=gettext_lazy("模型UID"))
