""""
根据账号密码登陆到gmail下载文件
create by swm 2018/09/12
"""
import json
import requests


class Gmail:

    def __init__(self, account, paaswd):
        self.account = account
        self.passwd = paaswd
        self.session = requests.Session()

    def G_identifier(self):
        params = (('hl', 'en'), ('_reqid', '60794'), ('rt', 'j'))
        headers = {
            'x-same-domain': '1',
            'origin': 'https://accounts.google.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'google-accounts-xsrf': '1',
            'cookie': 'GAPS=1:5anptsFCcX86o8zx79JaMKbjR6SUSg:i9ZZi85-G8eD7wsC; ',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'accept': '*/*',
            'referer': 'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
            'authority': 'accounts.google.com',
            'dnt': '1'
        }
        data = [
            ('continue', 'https://mail.google.com/mail/'),
            ('service', 'mail'),
            ('hl', 'en'),
            ('f.req',
             '["{email}","",[],null,"EG",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26app%3Ddesktop%26next%3D%252F%26action_handle_signin%3Dtrue&hl=en&service=youtube&passive=true&uilel=3",null,[],4,[],"GlifWebSignIn"],1,[null,null,[]],null,null,null,true],"{email}"]'.format(
                 email=self.account)),
            ('cookiesDisabled', 'false'),
            ('deviceinfo', '[null,null,null,[],null,"EG",null,null,[],"GlifWebSignIn",null,[null,null,[]]]'),
            ('gmscoreversion', 'undefined'),
            ('checkConnection', 'youtube:202:1'),
            ('checkedDomains', 'youtube'),
            ('pstMsg', '1')
        ]
        response = self.session.post('https://accounts.google.com/_/signin/sl/lookup', headers=headers,
                                       params=params, data=data)
        res = json.loads((response.text).replace(")]}'", ""))
        iden = res[0][0][2]
        return iden

    def login(self, identifier):
        params = (('hl', 'en'), ('_reqid', '260794'), ('rt', 'j'))
        headers = {
            'x-same-domain': '1',
            'origin': 'https://accounts.google.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'google-accounts-xsrf': '1',
            'cookie': 'GAPS=1:Q6gx2sQ34TRRxWUO3mC1_Be79xLYpA:akZ-LyOsSbAsOKOQ',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'accept': '*/*',
            'referer': 'https://accounts.google.com/signin/v2/sl/pwd?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&navigationDirection=forward',
            'authority': 'accounts.google.com',
            'dnt': '1',
        }
        data = [
            ('continue', 'https://mail.google.com/mail/'),
            ('service', 'mail'),
            ('hl', 'en'),
            ('f.req',
             '["{G_identifier}",null,1,null,[1,null,null,null,["{Password}",null,true]],[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26app%3Ddesktop%26next%3D%252F%26action_handle_signin%3Dtrue&hl=en&service=youtube&passive=true&uilel=3",null,[],4,[],"GlifWebSignIn"],1,[null,null,[]],null,null,null,true]]'.format(
                 G_identifier=identifier, Password=self.passwd)),
            ('cookiesDisabled', 'false'),
            ('deviceinfo', '[null,null,null,[],null,"EG",null,null,[],"GlifWebSignIn",null,[null,null,[]]]'),
            ('gmscoreversion', 'undefined'),
            ('checkConnection', 'youtube:202:1'),
            ('checkedDomains', 'youtube'),
            ('pstMsg', '1'),
        ]
        response = self.session.post('https://accounts.google.com/_/signin/sl/challenge', headers=headers,
                                       params=params, data=data)
        login = (response.text).replace(")]}'", "")
        print(login)
        print('/n')
        print(response)
        print('/n')
        print(response.cookies)

        # login = json.loads(login)
        # print(login)
        # rep = self.session.get("https://mail.google.com/mail/u/0/#inbox")
        # print(rep.text)
        # if "CheckCookie" in response:
        #     return 1
        # if str(login[0][0][5][5]) == "INCORRECT_ANSWER_ENTERED":
        #     return 0
        return


if __name__ == '__main__':
    ac = "sepjudy@gmail.com"
    pwd = "ADSZadsz123"
    gmail = Gmail(ac, pwd)
    identifier = gmail.G_identifier()
    print("获取授权码成功")
    print(identifier)
    login = gmail.login(identifier)

