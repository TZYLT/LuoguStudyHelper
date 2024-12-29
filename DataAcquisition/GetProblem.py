
import requests
import re
import json
from urllib.parse import unquote

f = open('problems.json', 'w')
res = []

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36 spider/0.1",
}


def getProblem(pid):
    return json.loads(requests.get(f"https://www.luogu.com.cn/problem/{pid}?_contentOnly=1", headers=headers).text)['currentData']


for i in range(2000, 2011):
    tmpdict = {}
    tmpdict["pid"] = f"P{i}"
    tmpdict["data"] = getProblem(f"P{i}")["problem"]
    res.append(tmpdict)

# print(res)
f.write(json.dumps(res, indent=4).replace("\\t", "    "))