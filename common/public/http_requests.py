import requests
class HttpRequest:
    @staticmethod
    def http_request(method,url,data=None,headers=None):
        if method == 'get':
            res = requests.get(url,data,headers=headers)
        elif method == 'post':
            res = requests.post(url,data,headers=headers)
        return res

if __name__ == '__main__':
    url = ' http://120.197.235.109/newsAppApi/1.0/ad/focus?belongCode=200&belongType=2'
    res = HttpRequest.http_request('get',url)
    print(res.json())