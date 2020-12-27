# get_repo.py get information from api
import requests
import json

# 执行api调用并且存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()  # 将返回的json格式通过json方法转化成字典
print("Total repositories:", response_dict['total_count'])

# 将信息写入
with open("result.txt", "w") as fp:
    fp.write(json.dumps(response_dict,indent=4))

