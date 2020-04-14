#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 10:49
# @Author  : FebSun
# @FileName: test_demo.py
# @Software: PyCharm
import json

import requests
from requests import Session, Response

proxies = {
    "http": "http://127.0.0.1:8998",
    "https": "http://127.0.0.1:8998"
}
url_get = "https://httpbin.testing-studio.com/get"

def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    print(r.status_code)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "csdcc"
                     })
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()["args"]["a"] == "1"


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      data={
                          "a": 2,
                          "b": 3,
                          "c": "2312312"
                      })
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))


def test_post_with_params():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      },
                      data={
                          "a": 2,
                          "b": 3,
                          "c": "dddd"
                      },
                      headers={"h": "head demo"})
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()["headers"]["H"] == "head demo"


def test_file():
    file = open("E:\\HogwartsSDET11\\test_requests\\__init__.py", "rb")
    r = requests.post("https://httpbin.testing-studio.com/post", files={"file": file})
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))


def test_upload():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      headers={"Content-Type": "application/plain"},
                      cookies={"name": "FebSun"})
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))


def test_proxy():
    r = requests.post("https://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "cccc"
                      },
                      data={
                          "a": 2,
                          "b": 3,
                          "c": "dddd"
                      },
                      proxies=proxies,
                      verify=False,
                      headers={"h": "head demo"})
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    assert r.json()["headers"]["H"] == "head demo"


def test_session():
    s = Session()
    s.proxies=proxies
    s.verify=False
    s.get(url_get)


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        # r.content = "OK HOOK SUCCESS"
        r.demo = "Demo Content"
        return r
    r = requests.get("https://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "csdcc"
                     },
                     hooks={"response": [modify_response]})
    print(json.dumps(r.json(), indent=2, ensure_ascii=False))
    print(r.demo)
