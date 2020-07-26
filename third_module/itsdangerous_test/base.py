# -*- coding:utf-8 -*-
import time

from itsdangerous import URLSafeSerializer, TimedJSONWebSignatureSerializer as jws_auth

SECRET_KEY = "8850f888-15d6-11ea-96f6-a0afbdb7e009"


def test_url_safe():
    url_serializer = URLSafeSerializer(secret_key=SECRET_KEY)
    token = url_serializer.dumps(dict(id=1, name="张三"))
    data = url_serializer.loads(token)
    print(data["name"])


def test_json_web_signature():
    auth = jws_auth(secret_key=SECRET_KEY, salt="My Salt", expires_in=5)  # 5分钟后过期
    token = auth.dumps(dict(id=2, name="LiSa"))
    token = token.decode()  # 转为字符串
    data = auth.loads(token, salt="My Salt")
    print(data["name"])
    time.sleep(6)
    data2 = auth.loads(token, salt="My Salt")
    print(data2["name"])


if __name__ == '__main__':
    test_url_safe()
    test_json_web_signature()
