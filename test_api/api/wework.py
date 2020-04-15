#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:30
# @Author  : FebSun
# @FileName: wework.py
# @Software: PyCharm
import requests

from api.baseapi import BaseApi


class WeWork(BaseApi):
    token = dict()
    secret = "hX4oeIqhP4w_knYbXM2QXe6AH6lEJ8WzKckr7XtpjBA"

    @classmethod
    def get_token(cls, secret=secret):
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            cls.token[secret] = r["access_token"]
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(
            cls.token_url,
            params={"corpid": cls.corpid, "corpsecret": secret}
        )
        cls.format_json(r)
        return r.json()