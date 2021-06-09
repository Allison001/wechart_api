import requests


class BasePage():

    def __init__(self):
        url = " https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2347fac9c4a29960&corpsecret=ODMt674VxHnSwe_82JNrm75CWituEFsbSg9saVD57rs"
        rr = requests.get(url)
        self.token = rr.json()['access_token']
        #创建session
        self.r = requests.session()
        #将token放入session
        self.r.params = {"access_token":self.token}


    def req(self,method,*args,**kwargs):
        return self.r.request(method,*args,**kwargs)