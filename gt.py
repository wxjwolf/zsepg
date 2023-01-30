import requests
import base64
import json


# 读取文件
def open_file(file_path):
    with open(file_path, 'rt') as f:
        return base64.b64encode(str(f.read(), 'UTF-8'))


# 将文件转换为base64编码，上传文件必须将文件以base64格式上传
def file_base64(data):
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64


# 上传文件
def upload_file(file_data):
    file_name = "zs.xml"  #文件名
    token = "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"
    url = "https://api.github.com/repos/wxjwolf/zsepg/contents/master/"+file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    content = file_data
    data = {
        "message": "message",
        "committer": {
            "name": "wxjwolf",
            "email": "wxjwolf@gmail.com"
        },
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    print(re_data)
    print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/[user]/[repo]/[path]"+file_name)
# 在国内默认的down_url可能会无法访问，因此使用CDN访问

fdata = open_file('zs.xml')
upload_file(fdata)