import requests
import time
import random

def select(cout):
    url = "https://bkzhjx.wh.sdu.edu.cn/jsxsd/xsxkkc/xxxkOper?kcid=sd01331110&cfbs=null&jx0404id=202420252001454&xkzy=&trjf="
    header = {
        "Cookie": "bzb_jsxsd=6B874C8651E22006C931D839CB47E7DF; SERVERID=128; bzb_njw=D886F252F4CA5D471CFE855263260553",
        "Referer": "https://bkzhjx.wh.sdu.edu.cn/jsxsd/xsxkkc/getXxxk",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    try:
        res = requests.get(url, headers=header, timeout=10)
        data = res.json()
        print(cout, ' ', data['message'])
        return data.get('success', False)
    except:
        print(cout, " 发生错误")
        time.sleep(5)
        return False


cout = 0
while True:
    cout += 1
    time.sleep(1.5 + random.random())
    res = select(cout)
    if res == 'true':
        break