import requests
#import re
import json
from lxml import etree
from datetime import datetime
#print(dt)

def get_program(pid):
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
    url="https://p.cztv.com/api/paas/program/{}/{}"
    ch = []
    dt=datetime.today().strftime("%Y%m%d")
    url1=url.format(pid,dt)
    with requests.request('GET',url1,headers = {'User-agent':ua}) as res:
        content = res.text
        load_data = json.loads(content)
        if load_data.get("message")=="success":
            data = load_data.get("content").get("list")[0].get("list")
            for i in data:
                endtime=float(i["play_time"]) + float(i["duration"]) 
                endtime1=datetime.fromtimestamp(endtime/1000.0).strftime("%Y%m%d%H%M%S") + " +0800" 
                ch.append({'channel':pid,'start':formattime(i["play_time"]),'stop':endtime1,'title':i["program_title"]})
    return ch;

def formattime(t):
       return datetime.fromtimestamp(float(t)/1000.0).strftime("%Y%m%d%H%M%S") + " +0800"      
#调用示例,chennelid为参数,返回dict,time and titile
#print(get_program("101"))