#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 21:33
# @Author  : FebSun
# @FileName: groupchat.py
# @Software: PyCharm
import json

import requests


class GroupChat:
    def list(self, token, offset=0, limit=10, **kwargs):
        list_json = {"offset": offset, "limit": limit}
        list_json.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={"access_token": token},
            json=list_json)
        return r.json()

    def get(self, token, chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": token},
            json={"chat_id": chat_id}
        )
        return r.json()
