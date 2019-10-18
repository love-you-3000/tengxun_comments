import requests
from urllib.parse import urlencode
import  json
import re
from tqdm import *
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
bash_url = 'https://video.coral.qq.com/filmreviewr/c/upcomment/q0t4yvm2i52eoub?'
f= open('result.txt','w')
page = 20
print('共爬取'+str(page)+'页：')
# 爬取的第一页的commentid参数，之后的改参数从前一页获取的数据中提取
commentid = '6051606569879688737'
# tqdm显示进度条
for i in tqdm(range(page)):
    try:
        parse = {
            'commentid': commentid,
            'reqnum': '3',
            'callback': 'jQuery112406841701832215665_1571365605027'
        }
        url = bash_url+urlencode(parse) # 构造url
        pat = 'jQuery.*?\((.*)\)'
        data =requests.get(url,headers=headers).text 
        json_dict =re.findall(pat,data)[0]
        texts = json.loads(json_dict) # 将数据改成json格式
        # 提取需要的内容
        commentid = (texts.get('data')).get('last') 
        for contents in (texts.get('data')).get('commentid'):
            title  = contents.get('title')
            abstract = contents.get('abstract')
            f.write(title+'\n')
            f.write(abstract+'\n')
            f.write('='*20+'\n')
    except Exception as err:
        print(err)

f.close()
time.sleep(1)
print('写入文件完成。')