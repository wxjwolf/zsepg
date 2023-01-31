import os
import jike#tvsou
import cctv
import tvzj
import time
import xml.etree.ElementTree as ET
from datetime import datetime
def sub_appendnode(root,ch,pid):
    #print(ch)
    for i in ch:
      programme = ET.Element("programme", {"start": i["start"],"stop": i["stop"],"channel": pid})
      title = ET.Element("title", {"lang":"zh"})
      title.text= i["title"]
      programme.append(title)
      title = ET.Element("desc", {"lang":"zh"})
      title.text= ""
      programme.append(title)
      root.append(programme)

def get_tname(t):
    ch={'CCTV5plus':'CCTV5+','CCTVjilu':'CCTV9','CCTVchild':'CCTV14'}
    ret=t
    if ch.__contains__(t):
        ret=ch[t]
    return ret
    
sourxml="/root/zsepg/channel.xml"
descxml="/root/py/zs.xml"
# 1、打开xml文件
tree = ET.parse(sourxml)
# 获xml文件的内容取根标签
root = tree.getroot()
root.set("last-update-time",datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
if os.path.isfile(descxml):
    os.remove(descxml)
#print(root)
for child in root: #获取根节点下的子标签
    #print(child.tag)      #  *.tag 是获取标签名字(字符串类型)
    pid=child.get('id')  #  *.attrib是获取标签属性（字典类型）
    pgroup=child.get('group')
    pname=child.findtext('display-name')
    if not pname:
        continue
    
    sub1=child.find('./display-name')
    sub1.text=get_tname(pname)
    print("处理 【 "+ sub1.text + " 】")
    if pgroup=="weishi":
        sub_appendnode(root,jike.get_program(pname,pid),pid)
    elif pgroup=="yangshi":
        sub_appendnode(root,cctv.get_program(pname.lower(),pid),pid)
    elif pgroup=="zj":
        sub_appendnode(root,tvzj.get_program(pid),pid)

tree.write(descxml, xml_declaration=True, encoding="utf-8")


