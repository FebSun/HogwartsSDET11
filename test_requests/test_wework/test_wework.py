#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 20:52
# @Author  : FebSun
# @FileName: test_wework.py
# @Software: PyCharm
import json

import requests

from test_wework.groupchat import GroupChat


class TestWeWork:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww8c015d6759a80a73"
    secret = "Qmvtz94bM2KXWW0_dE0vqz18l6Ay1jmqrtfSkdPd8Ck"
    token = None

    @classmethod
    def setup_class(cls):
        r = requests.get(
            cls.token_url,
            params={
                "corpid": cls.corpid,
                 "corpsecret": cls.secret
                 })
        cls.token = r.json()["access_token"]
        cls.groupchat = GroupChat()
        assert r.json()["errcode"] == 0

    def test_get_token_exist(self):
        assert self.token is not None

    def test_groupchat_get(self):
        r = self.groupchat.list(token=self.token)
        # print(json.dumps(r, indent=2))
        # chat_id = r["group_chat_list"][0]["chat_id"]
        assert r["errcode"] == 0

    def test_groupchat_detail(self):
        chat_id = self.groupchat.list(token=self.token)["group_chat_list"][0]["chat_id"]
        r = self.groupchat.get(token=self.token, chat_id=chat_id)
        print(json.dumps(r, indent=2))
        assert r["errcode"] == 0






