import requests
import re
import json
from urllib.parse import unquote

## Warning: This code only for testing. It can not work currently.
## 警告：此代码仅供测试使用，目前无法正常运行。

# 用户信息
uid = "" # 填入自己的uid
client_id = "" # 填入自己的client_id

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 Spider/0.1",
    "Cookie": "_uid="+uid+"; __client_id="+client_id+";" 
}

def get_problem_json(pid):
    try:
        # 发送HTTP GET请求
        response = requests.get(url=f"https://www.luogu.com.cn/record/list?user={pid}", headers=headers)
        response.raise_for_status()  # 如果响应状态码不是200，将引发HTTPError异常

        # 在响应文本中查找decodeURIComponent调用的内容
        matches = re.findall(r'decodeURIComponent\("(.*)"\)', response.text)
        print(response.text)
        if not matches:
            raise ValueError("未找到decodeURIComponent匹配的字符串")

        # 解码并解析JSON字符串
        json_str = unquote(matches[0])
        data = json.loads(json_str)

        # 检查'currentData'键是否存在
        if 'currentData' not in data:
            raise KeyError("JSON对象中缺少'currentData'键")

        return data['currentData']
    except requests.RequestException as e:
        print(f"请求错误: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解码错误: {e}")
    except (IndexError, ValueError, KeyError) as e:
        print(f"处理响应数据时发生错误: {e}")
    except Exception as e:
        print(f"发生未预料的错误: {e}")
    return None

# 调用函数并打印结果
data = get_problem_json(uid)
if data:
    print(json.dumps(data, sort_keys=True, indent=4))
else:
    print("未能获取数据")