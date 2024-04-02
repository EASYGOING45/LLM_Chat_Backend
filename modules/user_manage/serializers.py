# -*- coding: utf-8 -*-

from rest_framework import serializers


class UpdateUserRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
