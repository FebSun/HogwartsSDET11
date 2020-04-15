#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 20:30
# @Author  : FebSun
# @FileName: baseapi.py
# @Software: PyCharm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 19:14
# @Author  : FebSun
# @FileName: baseapi.py
# @Software: PyCharm
import json


class BaseApi:
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww8c015d6759a80a73"

    @classmethod
    def format_json(cls, r):
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))