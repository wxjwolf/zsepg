import requests
#import re
import json
from lxml import etree
from datetime import datetime
#print(dt)
def get_program(ccname,pid):
    ch = []
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    url="http://api.cntv.cn/epg/getEpgInfoByChannelNew?c={}&serviceId=tvcctv&d={}&t=jsonp&cb=setItem1"
    dt=datetime.today().strftime("%Y%m%d")
    url1=url.format(ccname,dt)
    #print(url1)
    with requests.request('GET',url1,headers = {'User-agent':ua}) as res:
        content = res.text
        if content.__contains__("channelName"):
            content=content.replace("setItem1(","").replace(");","")
            load_data = json.loads(content)
            data = load_data.get("data").get(ccname).get("list")#返回list
            for i in data:
                #print(formattime(i["play_time"]))#program_title
                ch.append({'channel':pid,'start':formattime(i["startTime"]),'stop':formattime(i["endTime"]),'title':i["title"]})
                #ch[formattime(i["startTime"])]=i["title"]
    #print(ch)
    return ch;

def formattime(t):
    #ret=datetime.fromtimestamp(float(t)/1000.0).strftime("%Y%m%d%H%M%S") + " +0800"  
    return datetime.fromtimestamp(float(t)/1000.0).strftime("%Y%m%d%H%M%S") + " +0800"   
#调用示例,chennelid为参数,返回dict,time and titile
#print(get_program("cctv1","1"))