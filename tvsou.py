import requests
import re
import json
from lxml import etree
from datetime import datetime
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
def get_churl(c_name):
    ret=""
    with requests.request('GET',"https://www.tvsou.com/epg/weishi/",headers = {'User-agent':ua}) as res:
        res.encoding='utf-8'
        content = res.text
        html = etree.HTML(content)
        titles = html.xpath( "//ul[@class='c_list_main']//a//text()")
        url_list=html.xpath( "//ul[@class='c_list_main']//a/@href")
        nodes=dict(zip(titles,url_list))
        for a,b in nodes.items():
            if c_name==a.strip():
                ret=b.strip()
                ret="https://www.tvsou.com" + ret.replace("weishi","ishot")
                break
    return ret;

def get_program(c_name,pid):
    url=get_churl(c_name)
    ch=[]
    if url!="":
        with requests.request('GET',url,headers = {'User-agent':ua}) as res:
            res.encoding='utf-8'
            content = res.text
            if content:
              html = etree.HTML(content)
              titles = html.xpath( "//div[@class='layui-tab-item layui-show']//tr/td[1]/text()")
              t_name = html.xpath( "//div[@class='layui-tab-item layui-show']//tr/td[2]/text()")
              #url_list=html.xpath( "//ul[@class='c_list_main']//a/@href")
              print("ok")
              dt=datetime.today().strftime("%Y%m%d")
              for a in range(len(titles)):
                  titles[a]=t_format(titles[a])
                  if a<len(titles)-1:
                      endtime=t_format(titles[a+1])
                  else:
                      endtime=t_format("235959")
                  ch.append({'channel':pid,'start':titles[a],'stop':endtime,'title':t_name[a]})
            #nodes=dict(zip(titles,t_name))
            #for a,b in nodes.items():
            #    print(a.strip(),b.strip())
    return ch;

def t_format(t1):
    dt=datetime.today().strftime("%Y%m%d")
    t2=dt + t1.replace(":","")
    return t2.ljust(14,"0") + " +0800"
#调用示例，频道名称为参数，返回dict,time and title
#print(get_program("广东卫视","33"))

