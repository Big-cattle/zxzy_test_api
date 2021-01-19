import hashlib
import datetime
import json
class Md5Vale:
    now = datetime.datetime.now()
    jm = {
            'now_time' : now.strftime("%Y%m%d%H%M%S"),
            'appkey' : '123456',
            'appSecret' : 'e10adc3949ba59abbe56e057f20f883e'
        }
    def md5vale(self):
        key = self.jm['appkey']+self.jm['now_time']+self.jm['appSecret']
        input_name = hashlib.md5()
        input_name.update(key.encode("utf-8"))
        self.jm['now_time']+='1'
        return input_name.hexdigest()

    def make_json(key):
        return json.dumps(key)

if __name__ == '__main__':
    print(Md5Vale().md5vale())
    print(Md5Vale().jm['now_time'])


