from ZXZY_API_AUTO.common.public.make_md5 import Md5Vale
import requests
class Token:
    @staticmethod
    def get_token():
        url = 'http://plus.buy.139.com/zyapi/user/login/validateCode?appKey=123456'
        values = {"head": {"appKey": "123456", "requestId": Md5Vale().jm['now_time'], "sign": Md5Vale().md5vale(),
                           "token": "",
                           "uuid": "tXmnAuw5XZXz7lKHVmKxEfwqqzxzjlSIkhVS"},
                  "data": {"mobile": "15820201397", "code": "147258"}}
        params = Md5Vale.make_json(values)
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url, params, headers=headers)
        return res.json()['data']['token']
