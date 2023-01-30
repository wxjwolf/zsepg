import requests
import base64


def xmlupload(post_data):
    fname="zs.xml"
    url="https://gitee.com/api/v5/repos/wxjwolf2023/zsepg/contents/{}".format(fname)
	formdata = {"access_token":post_data["token"],"content":post_data["content"],"message":post_data["message"]}
    r = requests.post(url=url,data=formdata)
    if r.status_code == 201:
        print("INFO:upload {} successful".format(post_data["path"]))
        return r.json()["content"]["download_url"]
    return None

def read_xml(fname):
    with open(fname,'r') as f:
        data = base64.b64encode(f.read())
    return {
        "content":data,
        "token":"52687fc122563a248ea67ac848bbec3d",
        "message":"zsiptvepg"
    }
def postxml(fname):
	post_data=read_xml(fname)
	xmlupload(post_data)
