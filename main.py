import requests
from lxml import etree
import time, os
import config
import json

def save_img(url, name):
    url = "http:{}".format(url)
    if not os.path.isdir("img"):
        os.mkdir("img")
    img_path = os.path.join(os.getcwd(), "img")
    r = requests.get(url, headers = config.head(config.img_temp))
    with open(os.path.join(img_path, name), 'wb') as f:
        f.write(r.content)
        print(name, "  done")
    time.sleep(3)

def test(page):
    t = str(int(time.time()))[:-2] + '558' 
    head = config.head()
    url = config.urldemo.format(str(page), t )
    r = requests.get(url ,headers = head )
    j = json.loads(r.text)
    for i in j["data"]["pic_list"]:
        try:
            or_picurl = i['original_pic']
            name = str(i['mid']) + '_' + i['sub_name'].replace(":",'') + '.' + or_picurl[-3:]
        except:
            continue
        if os.path.isfile(os.path.join(os.getcwd(),"img",name)):
            print("{} 已存在 跳过爬取".format(name))
            continue
        save_img(or_picurl, name)

def main():
    page = 1
    while page < 100:
        test(page)
        page += 1 

if __name__ == "__main__":
    main()