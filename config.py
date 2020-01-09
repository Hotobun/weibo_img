headtemp = '''
Cookie: SINAGLOBAL=5066284321061.312.1567187405998; login_sid_t=1d12afd081751d760436e978389d0060; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=7611152627114.353.1578563275333; ULV=1578563275338:6:1:1:7611152627114.353.1578563275333:1577449696063; ALF=1610099283; SSOLoginState=1578563283; SUB=_2A25zEoaEDeThGeRP71EU9i3EwjyIHXVQaf9MrDV8PUNbmtANLXHgkW9NThai32fJvAA-d1p6Dn9OGCQ0unJU2rMM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5uhs5Am8Hzb-UvEZwDQA0V5JpX5KzhUgL.FozpShefSoeR1K52dJLoI0jLxKMLBK-L1--LxK-LBK-L1hMLxKML1-2L1hBLxKML1K.LB.BLxK.LBKqL1KzLxK-LBKBLBoBNSoqES7tt; SUHB=0vJYTBe_qWEkoX; wvr=6; UOR=www.chinatelecom.com.cn,widget.weibo.com,graph.qq.com; webim_unReadCount=%7B%22time%22%3A1578565029093%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D
Host: s.weibo.com
Pragma: no-cache
Referer: https://s.weibo.com/pic?q=miku&Refer=Spic_box
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 
X-Requested-With: XMLHttpRequest'''

img_temp = '''Accept:image/webp,image/apng,image/*,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Cache-Control:no-cache
Connection:keep-alive
Host:wx2.sinaimg.cn
Pragma:no-cache
Referer:http://wx2.sinaimg.cn/
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400'''

def head(data = headtemp):
    # rtype : dict
    # 转换为可使用的json格式
    d = dict()
    for i in data.split("\n"):
        if i == "":
            continue
        index = i.index(":")
        d[i[:index]] = i[index+1 : ].strip()
    return d 

urldemo = "https://s.weibo.com/ajax_pic/list?q=保登心爱&page={}&_t=0&__rnd={}"

if __name__ == "__main__":
    print(head())