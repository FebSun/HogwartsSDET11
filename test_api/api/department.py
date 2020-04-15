#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:30
# @Author  : FebSun
# @FileName: department.py
# @Software: PyCharm
import requests

from api.wework import WeWork


class Department(WeWork):
    secret = "hX4oeIqhP4w_knYbXM2QXe6AH6lEJ8WzKckr7XtpjBA"

    def create(self, name, parentid, **kwargs):
        list_json = {"name": name, "parentid": parentid}
        list_json.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=list_json
        )
        return r

    def update(self, id, **kwargs):
        list_json = {"id": id}
        list_json.update(kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=list_json
        )
        return r

    def delete(self, id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(
            url,
            params={"access_token": self.get_token(self.secret), "id": id}
        )
        return r

    def list(self, id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(
            url,
            params={"access_token": self.get_token(self.secret), "id": id}
        )
        return r

