# 公   司：峦锘科技
# 作   者：潘浩
# 创建时间：2022/3/11 11:58
# 备   注：request_demo
import hashlib
import json
import random
import urllib
import requests

class BaiFy(object):
    def __init__(self, world):
        self.world = world
        self.appid = ''  # 填写你的appid
        self.secretKey = ''  # 填写你的密钥
        self.fromLang = 'auto'  # 原文语种
        self.toLang = 'en'  # 译文语种
        self.salt = random.randint(32768, 65536)
        self.myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    def get_data(self):
        sign = self.appid + self.world + str(self.salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            self.world) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(
            self.salt) + '&sign=' + sign
        res = requests.get(myurl)
        return res.text
    def run(self):
        res = self.get_data()
        self.parse_data(res)
    def parse_data(self, res):
        dict_data = json.loads(res)
        print(dict_data['trans_result'][0]['dst'])

if __name__ == '__main__':
    BaiFy1 = BaiFy('')
    while True:
        world = input('请输入中文我帮您翻译为英文：')
        if world == 'q':
            break
        BaiFy1.world = world
        BaiFy1.run()