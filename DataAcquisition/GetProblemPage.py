
import requests
import re
import json
import sys
import os
from urllib.parse import unquote

## Usage: python GetProblemPage.py <problem_id>
## Example: python GetProblemPage.py P1001
## Example: python GetProblemPage.py CF1010A
## Explanation: This script will get the problem page of the given problem id and save it as a json file in the ProblemFiles folder.

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4331.0 Safari/537.36 spider/0.1",
}

# 获取题目信息
def getProblem(pid):
    return json.loads(requests.get(f"https://www.luogu.com.cn/problem/{pid}?_contentOnly=1", headers=headers).text)['currentData']

# 检查输入是否合法
if len(sys.argv) != 2:
    print("Usage: python GetProblemPage.py <problem_id>")
    sys.exit(1)

# 检查题目是否存在，存在则获取题目信息。
tmpdict = {}
tmpdict["pid"] = f"{sys.argv[1]}"
tmpdict["data"] = getProblem(f"{sys.argv[1]}")["problem"]
res.append(tmpdict)

# 获取相对路径
relative_path = os.path.join("ProblemFiles", f"{sys.argv[1]}.json")
os.makedirs(os.path.dirname(relative_path), exist_ok=True)

# 保存题目信息到文件
f = open(relative_path, 'w')
res = []
f.write(json.dumps(res, indent=4).replace("\\t", "    "))
