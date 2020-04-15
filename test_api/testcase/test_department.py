#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:45
# @Author  : FebSun
# @FileName: test_department.py
# @Software: PyCharm
from jsonpath import jsonpath

from api.department import Department


class TestDepartment:
    secret = "hX4oeIqhP4w_knYbXM2QXe6AH6lEJ8WzKckr7XtpjBA"

    @classmethod
    def setup_class(cls):
        cls.department = Department()

    def test_list(self):
        r = self.department.list(1)
        self.department.format_json(r)
        assert r.json()["errcode"] == 0

    def test_create(self):
        r = self.department.create("苍青之剑", 1)
        self.department.format_json(r)
        print(r.json()['id'])
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "created"

    def test_update(self):
        id = self.department.create("我真的只是想打铁", 1).json()['id']
        r = self.department.update(id=id, name="自然秘语")
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "updated"

    def test_delete(self):
        r = self.department.list(1)
        self.department.format_json(r)
        delete_department = jsonpath(r.json(), '$..department[?(@.name=="自然秘语")]')
        print(delete_department)
        id = delete_department[0]["id"]
        r = self.department.delete(id)
        assert r.json()["errcode"] == 0
        assert r.json()["errmsg"] == "deleted"

