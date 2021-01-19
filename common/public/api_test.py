import unittest
from ZXZY_API_AUTO.common.public.http_requests import HttpRequest
from ZXZY_API_AUTO.common.public.make_md5 import Md5Vale
from ZXZY_API_AUTO.common.public.get_token import Token
from ddt import ddt,data
from ZXZY_API_AUTO.common.public.do_excel import DoExcel
from ZXZY_API_AUTO.common.public.get_log import GetLog
'''利用ddt框架获取数据，循环请求'''
@ddt
class ApiTest(unittest.TestCase):
    test_data = DoExcel.read_excel()
    @data(*test_data)
    def test_api(self,item):
        params = Md5Vale.make_json(eval(item['data']))    #将获取到的Excel数据进行json格式化，然后赋值给params
        headers = {'Content-Type':'application/json'} # 请求头
        res = HttpRequest.http_request(item['http_method'],item['url'],params,headers) #调用http_requests封装方法，进行接口请求
        print(res.json())  #打印接口请求结果
        
        '''断言'''
        try:
            self.assertEqual(str(item['expect']),res.json()['head']['respCode'])#期望值与接口返回参数做断言
            test_result = 'Pass'  #用于得出测试结果，并写入Excel表格中
        except Exception as e:
           GetLog().error_log("断言出错了，错误原因{}".format(e))
           test_result = 'Fail'  #用于得出测试结果，并写入Excel表格中
           raise e
        finally:
            DoExcel.write_excel(item['moudle'],item['id']+1,str(res.json()),test_result)  #将测试结果以及接口返回数据写入Excel中
           



if __name__ == '__main__':
    unittest.main()